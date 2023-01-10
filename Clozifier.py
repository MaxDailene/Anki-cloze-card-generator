import re

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

with open("output.csv", "w") as file:
    file.write("\n".join(clozed_sentences))