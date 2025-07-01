from collections import Counter
from io import BytesIO

from docx import Document


def read_docx(filepath):
    with open(filepath, "rb") as file:
        return Document(BytesIO(file.read()))


def find_outcast(doc_prop: dict):
    prop_freq = list(doc_prop.values())
    # check if all element of the list are the same
    if len(set(prop_freq)) == 1:
        # print("all pragraph indent are the same")
        return (None, "all pragraph indent are the same")

    count = Counter(prop_freq)

    most_common = max(count, key=count.get)

    outcast_values = [key for key in count if key != most_common]

    outcast_str = [txt for txt, val in doc_prop.items() if val in outcast_values]

    return outcast_str


def get_paragraph_text_key(para):
    text = para.text
    if not text:
        return None
    return " ".join(text.lstrip().split()[:5])
