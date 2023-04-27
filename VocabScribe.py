import requests
from bs4 import BeautifulSoup
import re

# Enter the Vocabulary.com link
url = input("Enter Vocabulary.com link: ")

# Get the HTML content of the webpage
response = requests.get(url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all words and their respective definitions
words = soup.find_all('a', class_='word')
definitions = soup.find_all('div', class_='definition')

# Create a list to store the words and their definitions
word_list = []
for i in range(len(words)):
    word = re.sub(r'\s+', ' ', words[i].text.strip())
    definition = re.sub(r'\s+', ' ', definitions[i].text.strip())
    word_list.append(word + '\t' + definition)

# Write the words and their definitions to a text file
filename = re.sub('[^\w\s-]', '', soup.title.text.strip())
filename = filename.replace(' ', '_') + '.txt'
with open(filename, 'w', encoding='utf-8') as f:
    f.write('\n'.join(word_list))

print(f"Words and definitions have been written to {filename}.")
