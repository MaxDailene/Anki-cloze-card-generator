import re
import csv

char1 = '['
char2 = ']'

with open("input.txt", "r", encoding='utf-8') as file:
    text = file.read()
    
sentences = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', text)

clozed_sentences = []

for sentence in sentences:
    cloze_sentence = sentence
    cloze_count = 0
    
    matches = re.findall(r'(\[.*?\])', sentence)
    
    if matches:
        for match in matches:
            cloze_count += 1
            cloze_text = match.strip(char1 + char2)
            cloze_sentence = cloze_sentence.replace(match, "{{c" + str(cloze_count) + "::" + cloze_text + "}}")
    
    clozed_sentences.append(cloze_sentence)

with open("output.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows([[s] for s in clozed_sentences])
