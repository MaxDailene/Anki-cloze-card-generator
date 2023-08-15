import os

def combine_text_files(input_files, combined_output_path):
    with open(combined_output_path, 'w', encoding='utf-8') as combined_output_file:
        for input_file in input_files:
            with open(input_file, 'r', encoding='utf-8') as file:
                combined_output_file.write(file.read())
            combined_output_file.write('\n')  # Add a separator between files

input_files = []

while True:
    input_name = input("Enter the name of a text file (without .txt extension), or 'done' to finish: ") + ".json_kanjioutput"
    if input_name.lower() == 'done.json_kanjioutput':
        break

    input_path = input_name + '.txt'
    if os.path.exists(input_path):
        input_files.append(input_path)
    else:
        print(f"File '{input_path}' not found in the working directory.")

if input_files:
    combined_output_path = 'combined_output.txt'
    combine_text_files(input_files, combined_output_path)
    print(f"Combined output saved to '{combined_output_path}'.")
else:
    print("No input files provided. No combined output generated.")
