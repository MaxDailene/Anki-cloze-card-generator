import requests
import json
from bs4 import BeautifulSoup

url = "https://a.4cdn.org/{board}/thread/{thread_id}.json"

url = url.format(board="a", thread_id=247553435)

response = requests.get(url)

thread = json.loads(response.text)

with open("thread.txt", "w", encoding="utf-8") as f:
    for post in thread["posts"]:
        if "com" in post:
            soup = BeautifulSoup(post["com"], "html.parser")
            text = soup.get_text()
            f.write(text)
            f.write("\n\n")

print("Thread saved to thread.txt.")
