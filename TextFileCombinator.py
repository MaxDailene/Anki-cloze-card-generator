import os

def combine_text_files():
    # Get a list of all text files in the working directory
    text_files = [file for file in os.listdir() if file.endswith('.txt')]

    # Sort the list of text files
    text_files.sort()

    combined_text = ""

    # Iterate through each text file and append its content to the combined_text
    for text_file in text_files:
        with open(text_file, 'r') as file:
            content = file.read()
            combined_text += content

    # Write the combined content to a new text file
    with open('combined.txt', 'w') as combined_file:
        combined_file.write(combined_text)

if __name__ == "__main__":
    combine_text_files()
    print("Text files combined and saved as 'combined.txt'")
