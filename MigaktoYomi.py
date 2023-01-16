import json

with open('Engrish.json', 'r', encoding='utf-8') as f:
    data1 = json.load(f)

converted_data = []

for entry in data1:
    term = entry['term']
    altterm = entry['altterm']
    pos = entry['pos']
    definition = entry['definition']
    examples = entry['examples']
    audio = entry['audio']
    
    new_entry = [term, altterm, pos, definition, examples, audio, "", ""]
    
    converted_data.append(new_entry)

with open('converted_file.json', 'w', encoding='utf-8') as f:
    json.dump(converted_data, f)