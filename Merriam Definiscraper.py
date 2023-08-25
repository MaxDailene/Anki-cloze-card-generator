import os
import re
from bs4 import BeautifulSoup
from selenium import webdriver

def get_definitions(soup):
    definitions = []
    
    vg_entries = soup.find_all(class_='vg-sseq-entry-item')
    
    for entry in vg_entries:
        span_definition = entry.find(class_='dtText')
        if span_definition:
            definition = span_definition.get_text(strip=True)
        else:
            definition = entry.get_text(strip=True)
        definitions.append(definition)
    
    return definitions

def format_definitions(definitions):
    formatted_defs = []
    
    for i, definition in enumerate(definitions, start=1):
        definition = re.sub(r'^\d+:\s*', f'{i}: ', definition)
        subdefs = re.findall(r'\b(\w+)\s*:\s*(.+?)(?=\s*\d|$)', definition)
        
        if subdefs:
            subdef_str = ""
            for j, subdef in enumerate(subdefs, start=97):  # ASCII code for 'a'
                subdef_str += f"{i}{chr(j)}. {subdef[1]}\n"
            formatted_defs.append(subdef_str)
        else:
            formatted_defs.append(re.sub(r'(?<=\d)\s*:\s*', '', definition))
    
    return formatted_defs

def choose_definition(definitions):
    for i, definition in enumerate(definitions, start=1):
        print(f"{i}: {definition}")
    
    choice = int(input("Enter the number of the definition you want: "))
    return choice - 1

def main():
    driver = webdriver.Chrome()
    
    while True:
        word = input("Enter a word (or 'quit' to exit): ").strip()
        
        if word.lower() == 'quit':
            break
        
        output_path = "output.txt"
        
        if os.path.exists(output_path):
            mode = "a"
        else:
            mode = "w"
        
        url = f"https://www.merriam-webster.com/dictionary/{word}"
        driver.get(url)
        
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        
        definitions = get_definitions(soup)
        
        if not definitions:
            print(f"Unable to find definitions for '{word}'. Please enter another word.")
            continue
        
        formatted_defs = format_definitions(definitions)
        
        chosen_index = choose_definition(formatted_defs)
        chosen_definition = formatted_defs[chosen_index]
        
        with open(output_path, mode, encoding="utf-8") as file:
            file.write("{}\t{}\n".format(word, re.sub(r'(?<=\d)\s*:\s*', '', chosen_definition)))
        
        print(f"Definition for '{word}' saved to 'output.txt'.")
    
    driver.quit()
    print("Exiting the program.")

if __name__ == "__main__":
    main()
