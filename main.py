from util import read_docx, find_outcast, get_paragraph_text_key
from indentation import get_indent_props
from font import get_font_props, get_font_size_props
from line_spacing import get_line_spacing_props

def match_outcast_text(doc_path, prop_func):
    doc = read_docx(doc_path)
    prop = prop_func(doc_path)
    outcast_str = find_outcast(prop)
    if not outcast_str:
        return([], "All values are consistent")
    return [
        para.text.replace("\t", "").replace("/", "") 
        for para in doc.paragraphs
        if get_paragraph_text_key(para) in outcast_str
    ]


# Example usage
if __name__ == "__main__":
    print("Indent outcasts:", match_outcast_text("Travel.docx", get_indent_props))
    print("Font outcasts:", match_outcast_text("Travel.docx", get_font_props))
    print("Line Spacing outcasts:", match_outcast_text("Travel.docx", get_line_spacing_props))
    print("Font Size outcasts:", match_outcast_text("Travel.docx", get_font_size_props))



map(lambda x: x*x, [1,2,3,4])
filter(lambda x: x//2, [1, 2, 3, 4, 5, 6])
map(lambda x: len(x), ["apple", "banana", "kiwi"])

prefix = ["a", "e", "i", "o", "u"]

string = ["apple", "apricot", "banana", "grape", "apply"]

list(lambda x: x.startswith(map(prefix)), string)

people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]

list(lambda x: sorted(x, x.keys()))

x= [1, 2, 3] 
y = [4, 5, 6]
list(zip(lambda x, y: x + y))

string=["John Doe", "Jane Smith", "Alice Johnson"]
sorted(string, key=map(lambda x: x.split(" ")[-1]))
