import re

with open("input.txt", "r+", encoding='utf-8') as f:
    text = f.read()
    new_text = re.sub(r"\{\{c\d+::(.*?)\}\}", r"\1", text)
    f.seek(0)
    f.write(new_text)
    f.truncate()
