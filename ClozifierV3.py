import re
import nltk
from nltk.tokenize import sent_tokenize

n = 5

def make_cloze_deletion(sentence, n):
    sentence = re.sub(r"[\/\\\";,.]", "", sentence)
    words = nltk.word_tokenize(sentence)
    result = []
    c_number = 1
    i = 0
    while i < len(words):
        j = i + n
        while j < len(words) and len(words[j]) < 3:
            j += 1
        result.append("{{c{}::".format(c_number) + " ".join(words[i:j]) + "}} ")
        c_number += 1
        i = j
    return "".join(result)

with open("input.txt", "r") as file:
    text = file.read()
    sentences = sent_tokenize(text)
    output = [make_cloze_deletion(sentence, n) for sentence in sentences]

with open("output.csv", "w", encoding='utf-8') as outfile:
    outfile.write("\n".join(output))
