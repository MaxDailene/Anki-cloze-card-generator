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
counter = 0
current_sentence_index = 0
while current_sentence_index < len(sentences):
    words_list = []
    for j in range(n):
        if current_sentence_index >= len(sentences):
            break
        sentence = sentences[current_sentence_index]
        sentence = re.sub(r"[\/\\\";]", "", sentence)
        words = sentence.split()
        for i, word in enumerate(words):
            if word.isnumeric():
                counter += 1
                words[i] = "{{c" + str(counter) + "::" + word + "}}"
            elif len(word) <= 7:
                continue
            else:
                counter += 1
                words[i] = "{{c" + str(counter) + "::" + word + "}}"
        words_list.append(" ".join(words))
        current_sentence_index += 1
        counter = 0
    clozed_sentences.append(" ".join(words_list))

with open("output.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows([[s] for s in clozed_sentences])
