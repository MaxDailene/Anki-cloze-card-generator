import nltk
import re
import csv

with open("input.txt", "a", encoding='utf-8') as file:
    file.write('\n.')
with open("input.txt", "r", encoding='utf-8') as file:
    text = file.read()

sentences = nltk.sent_tokenize(text)

clozed_sentences = []
counter = 0
for sentence in sentences:
    sentence = re.sub(r"[\/\\\";,]", "", sentence)
    words = sentence.split()
    for i, word in enumerate(words):
        if word.isnumeric():
            counter += 1
            words[i] = word[0] + "{{c" + str(counter) + "::" + word[1:] + "}}"
        elif len(word) <= 5:
            continue
        else:
            counter += 1
            words[i] = word[0] + "{{c" + str(counter) + "::" + word[1:] + "}}"
    clozed_sentences.append(" ".join(words))
    counter = 0

with open("output.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    clozed_sentences = clozed_sentences[:-1]
    writer.writerows([[s] for s in clozed_sentences])
