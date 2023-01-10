import nltk
import re
import csv

with open("words_to_delete.txt", "r") as file:
    words_to_delete = file.read().splitlines()
    
with open("input.txt", "r") as file:
    text = file.read()

sentences = nltk.sent_tokenize(text)

clozed_sentences = []
counter = 0
for sentence in sentences:
    sentence = re.sub(r"[\/\\\(\)\";,]", "", sentence)
    words = sentence.split()
    for i, word in enumerate(words):
        if word in words_to_delete:
            counter += 1
            words[i] = "{{c" + str(counter) + "::" + word + "}}"

    clozed_sentences.append(" ".join(words))
    counter = 0

with open("output.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    clozed_sentences = clozed_sentences[:-1]
    writer.writerows([[s] for s in clozed_sentences])