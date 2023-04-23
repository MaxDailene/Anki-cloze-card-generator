with open('input.txt', 'r+', encoding='utf-8') as file:
    text = file.read()
    file.seek(0) # Move the file pointer to the beginning of the file
    
    text = text.replace('\n', ' ')
    text = text.replace('. ', '.\n')
    
    file.write(text)
    file.truncate() # Remove any remaining text after the modified content
