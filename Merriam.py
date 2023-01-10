import requests
from bs4 import BeautifulSoup

url = "https://www.merriam-webster.com/dictionary/languid"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

headword = soup.find(class_='hword').text
definitions = [d.text for d in soup.find_all(class_='sense-content w-100')]

with open("output.txt", "w") as file:
    file.write(headword + "\n")
    for definition in definitions:
        file.write(definition)