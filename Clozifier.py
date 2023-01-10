import re
import csv

with open("input.txt", "r") as file:
    text = file.read()

sentences = re.split("[.!?]", text)

clozed_sentences = []
counter = 0
for sentence in sentences:
    sentence = re.sub(r"[\/\\\(\)\'\";,]", "", sentence)
    words = sentence.split()
    for i, word in enumerate(words):
        if len(word) <= 3:
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
