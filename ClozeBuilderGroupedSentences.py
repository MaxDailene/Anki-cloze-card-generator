import nltk
import re
import csv

n = 2  # Number of sentences to group together

with open("input.txt", "a", encoding='utf-8') as file:
    file.write('\n.')
with open("input.txt", "r", encoding='utf-8') as file:
    text = file.read()

sentences = nltk.sent_tokenize(text)

clozed_sentences = []
for i in range(0, len(sentences), n):
    group = sentences[i:i+n]
    group_clozes = []
    counter = 0
    for sentence in group:
        sentence = re.sub(r"[\/\\\";]", "", sentence)
        words = sentence.split()
        for i, word in enumerate(words):
            if word.isnumeric():
                counter += 1
                words[i] = "{{c" + str(counter) + "::" + word + "}}"
            elif len(word) <= 3:
                continue
            else:
                counter += 1
                words[i] = "{{c" + str(counter) + "::" + word + "}}"
        group_clozes.append(" ".join(words))
    clozed_sentences.append(" ".join(group_clozes))
        
with open("output.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows([[s] for s in clozed_sentences])
