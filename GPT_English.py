input_file_path = 'input.txt'
output_file_path = 'GPT_words.txt'

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    lines = input_file.readlines()
    word = definition = example = ""
    
    for line in lines:
        line = line.strip()
        
        if line.startswith("Example sentence: "):
            example = line[len("Example sentence: "):]
            output_line = f"{word}\t{definition}\t{example}\n"
            output_file.write(output_line)
        
        elif line:
            if ":" in line:
                word, definition = line.split(": ", 1)
            else:
                word = line

# Print a message indicating the task is complete
print("Extraction and writing to the output file is complete.")
