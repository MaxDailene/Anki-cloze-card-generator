import json

with open('Engrish.json', 'r', encoding='utf-8') as f:
    data1 = json.load(f)

converted_data = []

for entry in data1:
    expression = entry['term']
    reading = entry['altterm']
    tags = ""
    rule_ids = ""
    priority = 0
    glosses = entry['definition']
    new_entry = [expression, reading, tags, rule_ids, priority, glosses]
    converted_data.append(new_entry)

with open('converted_file.json', 'w', encoding='utf-8') as f:
    json.dump(converted_data, f)
