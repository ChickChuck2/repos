from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome("chromedriver.exe")

url = "https://brainly.com.br/"
ask = input("Sua pergunta\n>> ").replace(" ","+")

newurl = f"{url}app/ask?q={ask}"
driver.get(newurl)
driver.maximize_window()
driver.execute_script("window.stop();")

print(newurl)

soup = BeautifulSoup(driver.page_source, "html.parser")
searchresult = soup.find(class_="SearchResults__relativeWrapper--1Eb7W")

sg = searchresult.find(class_="sg-animation-fade-in-fast").find(class_="sg-flex sg-flex--full-width sg-flex--wrap sg-flex--margin-top-m")

for a in sg.find_all("a",href=True):
    tarefa_Id = a["href"]

tarefa_URL = f"{url}/{tarefa_Id}"

print(tarefa_URL)
driver.get(tarefa_URL)

tarefasoup = BeautifulSoup(driver.page_source, "html.parser")

question = tarefasoup.find(class_="brn-qpage-next-question-box").find(class_="sg-text sg-text--large sg-text--bold sg-text--break-words brn-qpage-next-question-box-content__primary").find("span")
print(question)