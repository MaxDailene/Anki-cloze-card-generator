import re

with open("input.txt", "r", encoding='utf-8') as f:
    text = f.read()

pattern = r"\{\{c\d+::(.+?)\}\}"

cloze_deletions = re.findall(pattern, text)

for deletion in cloze_deletions:
    text = re.sub(r"\{\{c\d+::" + re.escape(deletion) + r"\}\}", deletion, text)

with open("output.txt", "w", encoding='utf-8') as f:
    f.write(text)
