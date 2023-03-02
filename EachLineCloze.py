import nltk
import re
import csv

with open("input.txt", "a", encoding='utf-8') as file:
    file.write('\n.')
with open("input.txt", "r") as file:
    text = file.read()

lines = text.split("\n")

clozed_sentences = []
counter = 0
for line in lines:
    line = re.sub(r"[\/\\\";,]", "", line)
    words = line.split()
    for i, word in enumerate(words):
        if word.isnumeric():
            counter += 1
            words[i] = "{{c" + str(counter) + "::" + word + "}}"
        elif len(word) <= 5:
            continue
        else:
            counter += 1
            words[i] = "{{c" + str(counter) + "::" + word + "}}"
    clozed_sentences.append(" ".join(words))
    counter = 0

with open("output.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    clozed_sentences = clozed_sentences[:-1]
    writer.writerows([[s] for s in clozed_sentences])
