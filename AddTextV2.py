import csv

input_file = 'input.csv'
add_text = 'Text to add: '

with open(input_file, 'r', encoding='utf-8') as csv_in:
    reader = csv.reader(csv_in)
    rows = [row for row in reader]

with open(input_file, 'w', encoding='utf-8') as csv_out:
    writer = csv.writer(csv_out)
    for row in rows:
        sentence = add_text + row[0]
        writer.writerow([sentence])
