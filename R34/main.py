import requests
from bs4 import BeautifulSoup
from random import randint
import Downloader

rand = randint(1,4519300)
url = f"https://rule34.xxx/index.php?page=post&s=view&id={rand}"
page = requests.get(url)
d
def initDownload():
    Downloader.Downloader()

try:
    soup = BeautifulSoup(page.text, "html.parser")
    initDownload()
except:
    print("Não foi possivel soupar o site")

def getImageSrc():
    imagesrc = soup.find(class_="flexi").find("img").get("src")
    return imagesrc

def getTitle():
    title = soup.find("title").text[0:20]
    return title