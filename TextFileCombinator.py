import os

def combine_text_files():
    text_files = [file for file in os.listdir() if file.endswith('.txt')]
    text_files.sort()
    combined_text = ""
    for text_file in text_files:
        with open(text_file, 'r', encoding='utf-8') as file:
            content = file.read()
            combined_text += content
    with open('combined.txt', 'w', encoding='utf-8') as combined_file:
        combined_file.write(combined_text)
    for text_file in text_files:
        os.remove(text_file)

if __name__ == "__main__":
    combine_text_files()
    print("Text files combined and saved as 'combined.txt'. Individual files deleted.")
