import re

def remove_substring(file_path, output_path, target):
    with open(file_path, "r") as f:
        text = f.read()

    text = re.sub(f'\\b({target})\\b', "", text)

    with open(output_path, "w") as f:
        f.write(text)

remove_substring("input.txt", "output.txt", "substring_to_remove")