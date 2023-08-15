import json

json_file_path = 'n5.json'
output_file_path = 'quiz_output.txt'

with open(json_file_path, encoding='utf-8') as json_file:
    data = json.load(json_file)

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for card in data['cards']:
        question = card['question']
        answers = card['answer']
        meaning = card['meaning']
        if len(answers) > 1:
            for i, answer in enumerate(answers):
                suffix = f' ({i+1})' if i > 0 else ''
                output_file.write(f'{question}{suffix}\t{answer}\t{meaning}\n')
        else:
            output_file.write(f'{question}\t{answers[0]}\t{meaning}\n')
