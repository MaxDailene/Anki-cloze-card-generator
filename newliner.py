file_name = 'input.txt'
char_to_add = '\n'
n = 5

with open(file_name, 'r', encoding='utf-8') as file:
    lines = file.readlines()

with open(file_name, 'w', encoding='utf-8') as file:
    for i, line in enumerate(lines):
        file.write(line)
        if (i + 1) % n == 0:
            file.write(char_to_add)
