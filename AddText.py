import csv


input_file = 'input.csv'
output_file = 'output.csv'
add_text = 'Text to add: '

with open(input_file, 'r', encoding='utf-8') as csv_in:
    reader = csv.reader(csv_in)
    with open(output_file, 'w') as txt_out:
        for row in reader:
            sentence = add_text + row[0]
            txt_out.write(sentence + '\n')
