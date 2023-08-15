import json

def process_json(json_file_path, output_file):
    with open(json_file_path, encoding='utf-8') as json_file:
        data = json.load(json_file)

    for card in data['cards']:
        question = card['question']
        answers = card['answer']
        if len(answers) > 1:
            for i, answer in enumerate(answers):
                output_file.write(f'{question} ({i+1})\t{answer}\n')
        else:
            output_file.write(f'{question}\t{answers[0]}\n')

def main():
    extract_multiple = input("Do you want to extract multiple JSON files? (yes/no): ").lower() == 'yes'

    if extract_multiple:
        output_paths = []

        while True:
            json_file_name = input("Enter the JSON file name (without .json extension), or 'done' to finish: ")
            
            if json_file_name.lower() == 'done':
                break
            
            json_file_path = json_file_name + '.json'
            output_file_path = json_file_path + '_kanjioutput.txt'
            
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                process_json(json_file_path, output_file)
            
            output_paths.append(output_file_path)
        
        print("Extraction completed.")
    else:
        json_file_name = input("Enter the JSON file name (without .json extension): ")
        json_file_path = json_file_name + '.json'
        output_file_path = json_file_path + '_kanjioutput.txt'
        
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            process_json(json_file_path, output_file)
        
        print("Extraction completed.")

if __name__ == "__main__":
    main()
