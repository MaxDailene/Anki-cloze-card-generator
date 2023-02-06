import re
import csv

with open("input.txt", "r", encoding='utf-8') as file:
    text = file.read()

delimiter = "##" # the character to use as a delimiter
clozed_sentences = []
counter = 0
for line in text.split(delimiter):
    line = line.strip()
    line = line.replace("\n", "<br>") # replace linebreaks with <br>
    words = re.sub(r"[\/\\\"]", "", line).split()
    for i, word in enumerate(words):
        if word.isnumeric():
            counter += 1
            words[i] = "{{c" + str(counter) + "::" + word + "}}"
        elif len(word) <= 3:
            continue
        else:
            counter += 1
            words[i] = "{{c" + str(counter) + "::" + word + "}}"
    clozed_sentences.append(" ".join(words))
    counter = 0

with open("output.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows([[s] for s in clozed_sentences])