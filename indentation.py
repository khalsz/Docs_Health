from docx import Document
from io import BytesIO
from collections import Counter

from util import read_docx, find_outcast, get_paragraph_text_key

def get_indent_props(doc_path):
    doc = read_docx(doc_path)

    indent_prop = {}

    for para in doc.paragraphs:
        key = get_paragraph_text_key(para)
        if not key:
            continue
        indent_length = len(para.text) - len(para.text.lstrip())
        indent_prop[key] = indent_length
    return indent_prop


# def match_outcast_txt(doc_path):
#     doc = read_docx(doc_path)
#     indent_prop = get_para_indent(doc_path)
#     outcast_str = find_outcast(indent_prop)

#     if not outcast_str:
#         print("all prargraph same")
#         return ([], "all prargraph indentations are teh same")

#     outcast_match = [
#         para.text.replace("\t", "").replace("/", "") for para in doc.paragraphs 
#         if " ".join(para.text.lstrip().split()[:5]) in outcast_str
#         ]
#     return outcast_match


if __name__ == "__main__":

    print(match_outcast_txt("Travel.docx"))