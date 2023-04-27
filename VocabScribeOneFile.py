import requests
from bs4 import BeautifulSoup
import re

url = input("Enter Vocabulary.com link: ")

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

wordlist = soup.find_all('li', class_='wordlist')
if wordlist:
    links = []
    for li in wordlist:
        header = li.find('div', class_='header')
        if header:
            h2 = header.find('h2')
            if h2 and h2.find('a'):
                link = "https://www.vocabulary.com/" + h2.find('a')['href']
                links.append(link)

    word_list = []
    for link in links:
        response = requests.get(link)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        words = soup.find_all('a', class_='word')
        definitions = soup.find_all('div', class_='definition')
        examples = soup.find_all('div', class_='example')
        for i in range(len(words)):
            word = re.sub(r'\s+', ' ', words[i].text.strip())
            definition = re.sub(r'\s+', ' ', definitions[i].text.strip())
            example = re.sub(r'\s+', ' ', examples[i].text.strip())
            word_list.append(word + '\t' + definition + '\t' + example)
    filename = re.sub('[^\w\s-]', '', soup.title.text.strip())
    filename = filename.replace(' ', '_') + '.txt'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(word_list))
    print(f"Words, definitions, and examples have been written to {filename}.")
else:
    words = soup.find_all('a', class_='word')
    definitions = soup.find_all('div', class_='definition')
    examples = soup.find_all('div', class_='example')

    word_list = []
    for i in range(len(words)):
        word = re.sub(r'\s+', ' ', words[i].text.strip())
        definition = re.sub(r'\s+', ' ', definitions[i].text.strip())
        example = re.sub(r'\s+', ' ', examples[i].text.strip())
        word_list.append(word + '\t' + definition + '\t' + example)

    filename = re.sub('[^\w\s-]', '', soup.title.text.strip())
    filename = filename.replace(' ', '_') + '.txt'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(word_list))

    print(f"Words, definitions, and examples have been written to {filename}.")