from util import read_docx
from util import get_paragraph_text_key

# Line-spacing-specific
def get_line_spacing_props(doc_path):
    doc = read_docx(doc_path)
    spacing_prop = {}
    for para in doc.paragraphs:
        key = get_paragraph_text_key(para)
        if not key:
            continue
        spacing = para.paragraph_format.line_spacing
        spacing_prop[key] = spacing if spacing is not None else "Default"
    return spacing_prop