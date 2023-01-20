import nltk
import re
import csv

start_char = "#"

with open("input.txt", "a", encoding='utf-8') as file:
    file.write('\n.')
with open("input.txt", "r", encoding='utf-8') as file:
    text = file.read()

sentences = nltk.sent_tokenize(text)

clozed_sentences = []
counter = 0
for sentence in sentences:
    if start_char in sentence:
        sentence = sentence.split(start_char)
        before, after = sentence[0], sentence[1]
        after = re.sub(r"[\/\\\"]", "", after)
        after = after.lstrip()
        after = after.replace("  ", " ")
        words = after.split()
        for i, word in enumerate(words):
            if word.isnumeric():
                counter += 1
                words[i] = word[0] + "{{c" + str(counter) + "::" + word[1:] + "}}"
            elif len(word) <= 5:
                continue
            else:
                counter += 1
                words[i] = word[0] + "{{c" + str(counter) + "::" + word[1:] + "}}"
        clozed_sentences.append(before + " " + " ".join(words))
    else:
        clozed_sentences.append(sentence)
    counter = 0


...
with open("output.csv", "w", newline='', encoding='utf-8') as file:
    clozed_sentences = [re.sub(r"\s+", " ", sentence) for sentence in clozed_sentences]
    clozed_sentences = clozed_sentences[:-1]
    writer = csv.writer(file)
    writer.writerows([[s] for s in clozed_sentences])
