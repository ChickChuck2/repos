from main import getTitle, getImageSrc
import requests

def Downloader():
    with open(f"{getTitle()}.jpg", "wb") as handle:
        response = requests.get(getImageSrc(), stream=True)

        if not response.ok:
            print(response)
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)