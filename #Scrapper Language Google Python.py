#Scrapper Language Google Python
import requests
from bs4 import BeautifulSoup

langS = "pt-BR"
page = requests.get(f"https://translate.google.com.br/m?sl=pt&tl=en&mui=sl&hl={langS}")

soup = BeautifulSoup(page.text, 'html.parser')

langList = soup.find_all("a", href=True)
langLis = { }
i = 0
for lang in langList:
    
    href = lang['href']
    Title = lang.text
    sl = href.split('sl=')[1].replace('./m?','').replace("&tl=en&hl=pt-BR","")
    i = i + 1
    print(sl)
    if i > 2:
        langLis.update({f"{Title}":f"{sl}"})

try:
    f = open(f"{langS}.txt","a")
    for lang in langLis:
        f.write(f'{langLis[lang]},       "{lang}",\n')
    f.close()

except Exception as e:
    f = open(f"{langS}.txt","x")
print("Pronto!")