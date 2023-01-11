import re

def clean_text_inplace(file_path):
    with open(file_path, "r") as file:
        text = file.read()

    cleaned_text = re.sub(r'\[.*?\]', '', text)

    with open(file_path, "w") as file:
        file.write(cleaned_text)

clean_text_inplace("input.txt")
