import re

def clean_text(file_path):
    with open(file_path, "r") as file:
        text = file.read()

    cleaned_text = re.sub(r'([a-z])\s+(?=[A-Z])', r'\1 ', text)
    cleaned_text = re.sub(r'[\r\n]+', '\n', cleaned_text)

    output_path = "cleaned_" + file_path
    with open(output_path, "w") as output_file:
        output_file.write(cleaned_text)


clean_text("input.txt")
