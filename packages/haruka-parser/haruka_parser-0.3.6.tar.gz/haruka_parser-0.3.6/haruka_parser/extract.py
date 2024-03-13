import os
import re
from collections import defaultdict
from typing import Dict
from haruka_parser.readablity_lxml import Document
from resiliparse.parse.html import HTMLTree
from resiliparse.extract.html2text import extract_plain_text
from inscriptis import ParserConfig
from inscriptis.css_profiles import CSS_PROFILES
from inscriptis.html_engine import Inscriptis
from inscriptis.model.html_document_state import HtmlDocumentState
from inscriptis.model.tag.a_tag import a_start_handler, a_end_handler
from inscriptis.model.tag.br_tag import br_start_handler
from inscriptis.model.tag.img_tag import img_start_handler
from inscriptis.model.tag.list_tag import (
    ul_start_handler,
    ol_start_handler,
    li_start_handler,
    ul_end_handler,
    ol_end_handler,
)
from inscriptis.model.tag.table_tag import (
    table_start_handler,
    tr_start_handler,
    td_start_handler,
    table_end_handler,
    td_end_handler,
)
import ftfy
from inscriptis.model.tag import CustomHtmlTagHandlerMapping
from inscriptis.model.html_document_state import HtmlDocumentState


from haruka_parser.latex_processing import (
    extract_math,
    extract_delimited_math,
    get_math_config,
)
from haruka_parser.tree_processing import (
    remove_jax_ignore,
    remove_buttons,
    remove_image_figures,
    extract_code,
    extract_tables,
    extract_headings,
    remove_dense_links,
    add_se_separators,
    wikipedia_preprocess,
    remove_display_none,
    main_content_preprocess,
    post_process_headings,
    get_title,
    get_lxml_tree,
    extract_time,
)
from haruka_parser.line_processing import (
    remove_empty_headers,
    remove_edit_buttons,
    remove_chinese_characters,
    remove_boilerplate,
    restore_replacements,
)
from haruka_parser.utils import ReplacementManager

DEFAULT_CONFIG = defaultdict(
    bool,
    {
        "add_title": True,
        "readability": False,
        "skip_large_links": False,
        "extract_latex": True,
        "extract_cnki_latex": False,
        "escape_dollars": True,
        "remove_buttons": True,
        "remove_edit_buttons": True,
        "remove_image_figures": True,
        "markdown_code": False,
        "markdown_headings": True,
        "remove_chinese": False,
        "boilerplate_config": {
            "enable": False,
            "ratio_threshold": 0.18,
            "absolute_threshold": 10,
            "end_threshold": 15,
        },
    },
)

selectors_path = os.path.join(
    os.path.dirname(__file__), "dictionary/banned_selectors.txt"
)
with open(selectors_path, "r") as f:
    selectors = [line.replace("\n", "").strip() for line in f]
    # Remove empty lines
    selectors = [line for line in selectors if line]


def filter_tree(tree, replacement_manager, config, info):
    """Filters the HTML tree to remove unwanted elements."""

    # Remove display none elements
    remove_display_none(tree)

    # Remove the wikipedia footer
    wikipedia_preprocess(tree)

    if config["remove_buttons"]:
        # Remove any bootstrap buttons
        remove_buttons(tree)

    if config["remove_image_figures"]:
        # Remove any figures that only contain images
        remove_image_figures(tree)

    # Wrap the code in markdown code blocks
    info = extract_code(tree, replacement_manager, info, config["markdown_code"])

    if config["extract_latex"]:
        remove_jax_ignore(tree)

    # Record the location of headings and format them
    extract_headings(tree, replacement_manager, config["markdown_headings"])

    # Remove link lists
    remove_dense_links(tree)

    # Format tables
    _, info = extract_tables(tree.document, replacement_manager, config, info)

    # Process stack exchange separators
    add_se_separators(tree)

    # Preprocess main content
    main_content_preprocess(tree)

    return tree, info


def replace_tags(html, old, new):
    pattern = re.compile(old, re.IGNORECASE)
    return pattern.sub(new, html)


def html_preprocessing(html, config):
    if config["extract_cnki_latex"]:
        # Replace consecutive subscript tags
        html = re.sub(r"_(.*?)_", r"\1", html)
        # Replace italic tags
        html = re.sub(r"<i>(.*?)</i>", r"\1", html)
        # latex_str = re.sub(r"<i>(.*?)</i>", r"$\1$", latex_str)

        html = re.sub(
            r"(<sub>(.*?)</sub>)+",
            # lambda m: "_{" + "".join(re.findall(r"<sub>(.*?)</sub>", m.group(0))) + "}",
            lambda m: "[extract_itex]"
            + "_{"
            + "".join(re.findall(r"<sub>(.*?)</sub>", m.group(0)))
            + "}"
            + "[/extract_itex]",
            html,
        )
        html = re.sub(
            r"(<sup>(.*?)</sup>)+",
            lambda m: "[extract_itex]"
            + "^{"
            + "".join(re.findall(r"<sup>(.*?)</sup>", m.group(0)))
            + "}"
            + "[/extract_itex]",
            html,
        )
    html = replace_tags(html, "<template", "<div")
    html = replace_tags(html, "</template", "</div")
    html = replace_tags(html, "<frameset", "<div")
    html = replace_tags(html, "</frameset>", "</div>")
    html = html.replace("&lt;math&gt;", "[itex]")
    html = html.replace("&lt;/math&gt;", "[/itex]")
    html = html.replace("$", "[extract_single_dollar]")
    html = html.replace("§", "[extract_single_chapter]")
    return html


def extract_text(html, config=DEFAULT_CONFIG):
    """Extracts plain text from an HTML string."""
    
    def _start_li(state: HtmlDocumentState, _: Dict) -> None:
        """Handle the <li> tag."""
        pass

    info = {
        "found_math": False,
        "script_math_tex": 0,
        "script_math_asciimath": 0,
        "math_annotations": 0,
        "math_alttext": 0,
        "mathml": 0,
        "mathjax_tag": 0,
        "mathjax_inline_tex": 0,
        "mathjax_display_tex": 0,
        "mathjax_asciimath": 0,
        "img_math": 0,
        "codecogs_latex": 0,
        "wp_latex": 0,
        "mimetex.cgi": 0,
        "/images/math/codecogs": 0,
        "mathtex.cgi": 0,
        "other_latex_img": 0,
        "katex": 0,
        "math-container": 0,
        "wp-katex-eq": 0,
        "align": 0,
        "equation": 0,
        "x-ck12": 0,
        "texerror": 0,
        "code_block": 0,
        "table": 0,
        "chinese_table": 0,
        "title": "",
        "time": "",
    }

    if not html:
        return "", info

    # NFCK normalization
    html = ftfy.fix_text(html)

    pre_process_resiliparse_tree = HTMLTree.parse(html)
    pre_process_tree = get_lxml_tree(html)

    # TODO: Using the same tree parser
    try: info["title"] = get_title(pre_process_resiliparse_tree)
    except: pass
    try: info["time"] = extract_time(html, pre_process_tree)
    except: pass

    if config["readability"]:
        html = Document(pre_process_tree).summary()

    html = html_preprocessing(html, config)
    tree = HTMLTree.parse(html)
    replacement_manager = ReplacementManager()

    if config["skip_large_links"]:
        links = tree.document.query_selector_all("a")
        span_links = tree.document.query_selector_all("span a")
        if len(links) > 3000 or len(span_links) > 3000:
            print("Too many links, skipping")
            return None, None

    if config["extract_latex"]:
        math_config = get_math_config(tree.document.html)
        tree, info = extract_math(tree, replacement_manager, info)
    tree, info = filter_tree(tree, replacement_manager, config, info)

    lxml_tree = get_lxml_tree(str(tree))
    if lxml_tree is not None:
        # info["title"] = info["title"] or restore_replacements(
        #     get_title(lxml_tree), replacement_manager, config
        # )
        parser_config = ParserConfig(
            css=CSS_PROFILES["strict"], 
            display_images=False,
            custom_html_tag_handler_mapping=CustomHtmlTagHandlerMapping(
                start_tag_mapping={
                    "li": _start_li,
                },
                end_tag_mapping={}
            )
        )
        text = Inscriptis(
            lxml_tree,
            parser_config,
        ).get_text()
        info["html_parser"] = "inscriptis"
    else:
        # Disable their filters because we use our own.
        text = extract_plain_text(
            tree, main_content=True, alt_texts=False, skip_elements=selectors
        )
        info["html_parser"] = "resiliparse"

    if config["extract_latex"]:
        text = extract_delimited_math(text, math_config, info, replacement_manager)

    text = post_process_headings(text)

    lines = text.split("\n")

    if config["remove_chinese"]:
        # Remove Chinese characters
        lines = remove_chinese_characters(lines)

    if config["boilerplate_config"]["enable"]:
        # Remove boilerplate
        lines = remove_boilerplate(
            lines, config["boilerplate_config"], replacement_manager
        )

    # Remove headings with nothing (or only other headings) after
    lines = remove_empty_headers(lines, replacement_manager)

    # Strip lines
    lines = [line.rstrip() for line in lines]

    # Create the final string
    text = "\n".join(lines)

    if config["remove_edit_buttons"]:
        # Remove edit buttons
        lines = text.split("\n")
        lines = remove_edit_buttons(lines)
        text = "\n".join(lines)

    text = restore_replacements(text, replacement_manager, config, info)
    # If there are over two newlines in a row, replace with two
    text = re.sub(r"\n{3,}", "\n\n", text)

    text = text.strip()

    if config["add_title"] and info["title"]:
        if info["title"] not in "\n".join(text.split("\n")[:3]):
            if config["markdown_headings"]:
                text = "# " + info["title"] + "\n\n" + text
            else:
                text = info["title"] + "\n\n" + text

    return text, info
