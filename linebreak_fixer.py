with open('input.txt', 'r', encoding='utf-8') as input_file:
    text = input_file.read()

text = text.replace('\n', ' ')
text = text.replace('. ', '.\n')

with open('output.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(text)
