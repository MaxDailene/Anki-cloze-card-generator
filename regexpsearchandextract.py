import re

pattern = re.compile(r'(?<=<b>).*?(?=<\/b>)')

with open("input.txt", "r", encoding='utf-8') as f:
    content = f.readlines()

with open("output.txt", "w", encoding='utf-8') as f:
    for line in content:
        matches = pattern.findall(line)
        for match in matches:
            f.write(match + '\n')
