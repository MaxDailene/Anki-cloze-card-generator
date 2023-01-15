from bs4 import BeautifulSoup

with open("file.txt") as f:
    soup = BeautifulSoup(f, "lxml")

text = soup.get_text()

with open("file.txt", "w", encoding='utf-8') as out:
    out.write(text)
