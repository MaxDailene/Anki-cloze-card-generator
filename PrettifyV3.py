from bs4 import BeautifulSoup

with open("input.txt") as f:
    soup = BeautifulSoup(f, "lxml")

text = soup.get_text()

with open("input.txt", "w", encoding='utf-8') as out:
    out.write(text)
