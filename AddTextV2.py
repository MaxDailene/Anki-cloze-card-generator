import csv

input_file = 'input.txt'
output_file = 'output.txt'
add_text = '<b>p<br>'

with open(input_file, 'r', encoding='utf-8') as txt_in:
    with open(output_file, 'w', encoding='utf-8') as txt_out:
        for line in txt_in:
            sentence = add_text + line
            txt_out.write(sentence)
