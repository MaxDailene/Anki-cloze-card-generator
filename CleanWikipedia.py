import re
import os

def clean_text(file_path):
    with open(file_path, "r") as file:
        text = file.read()

    cleaned_text = re.sub(r'\[.*?\]', '', text)

    output_path = "cleaned_" + file_path
    with open(output_path, "w") as output_file:
        output_file.write(cleaned_text)

clean_text("input.txt")
os.remove("input.txt")
os.rename("cleaned_input.txt", "input.txt")
