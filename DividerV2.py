import nltk

def separate_sentences(input_file):
    with open(input_file, 'r') as file:
        text = file.read()

    sentences = nltk.sent_tokenize(text)

    with open(input_file, 'w',encoding='utf-8') as file:
        for sentence in sentences:
            file.write(sentence + '\n')

separate_sentences('input.txt')
