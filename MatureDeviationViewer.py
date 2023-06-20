import requests
import webbrowser

def open_deviantart_image(link):
    api_url = "https://backend.deviantart.com/oembed?url="
    full_url = api_url + link

    response = requests.get(full_url)
    data = response.json()
    image_url = data["url"]

    image_url = image_url.replace("\\", "")

    webbrowser.open(image_url)

link = input("Enter the DeviantArt link: ")
open_deviantart_image(link)
