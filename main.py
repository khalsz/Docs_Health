from font import get_font_props, get_font_size_props
from indentation import get_indent_props
from line_spacing import get_line_spacing_props
from util import find_outcast, get_paragraph_text_key, read_docx


def match_outcast_text(doc_path, prop_func):
    doc = read_docx(doc_path)
    prop = prop_func(doc_path)
    outcast_str = find_outcast(prop)
    if not outcast_str:
        return ([], "All values are consistent")
    return [
        para.text.replace("\t", "").replace("/", "")
        for para in doc.paragraphs
        if get_paragraph_text_key(para) in outcast_str
    ]


# Example usage
if __name__ == "__main__":
    print("Indent outcasts:", match_outcast_text("Travel.docx", get_indent_props))
    print("Font outcasts:", match_outcast_text("Travel.docx", get_font_props))
    print(
        "Line Spacing outcasts:",
        match_outcast_text("Travel.docx", get_line_spacing_props),
    )
    print("Font Size outcasts:", match_outcast_text("Travel.docx", get_font_size_props))
