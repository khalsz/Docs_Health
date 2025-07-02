from util import read_docx
from util import get_paragraph_text_key
from docx.shared import Pt

# Font-type-specific
def get_font_props(doc_path):
    doc = read_docx(doc_path)
    font_prop = {}
    for para in doc.paragraphs:
        key = get_paragraph_text_key(para)
        if not key or not para.runs:
            continue
        font_name = para.runs[0].font.name or "Unknown"
        font_prop[key] = font_name
    return font_prop


def get_font_size_props(doc_path):
    doc = read_docx(doc_path)
    font_size_prop = {}

    for para in doc.paragraphs:
        key = get_paragraph_text_key(para)
        if not key:
            continue

        sizes = []
        for run in para.runs:
            if run.font.size:
                sizes.append(run.font.size.pt)  # Convert from Emu to pt
        if sizes:
            avg_size = round(sum(sizes) / len(sizes), 2)
        else:
            avg_size = "Default"

        font_size_prop[key] = avg_size

    return font_size_prop