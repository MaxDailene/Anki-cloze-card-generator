import re
import nltk

from nltk.tokenize import word_tokenize

n = 5

def make_cloze_deletion(sentence, n):
    sentence = re.sub(r"[\/\\\";,.]", "", sentence)
    words = word_tokenize(sentence)
    result = []
    c_number = 1
    i = 0
    while i < len(words):
        j = i + n
        while j < len(words) and len(words[j]) < 3:
            j += 1
        result.append("{{c" + str(c_number) + "::" + " ".join(words[i:j]) + "}}" + " ")
        c_number += 1
        i = j
    return "".join(result)

with open("input.txt", "r", encoding='utf-8') as file:
    with open("output.csv", "w", encoding='utf-8') as outfile:
        for line in file:
            output = make_cloze_deletion(line, n)
            outfile.write(output + "\n")
