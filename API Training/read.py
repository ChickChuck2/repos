import requests

r = requests.get('https://api.hgbrasil.com/weather')

data = r.json()


result = data["results"]

forecastday = result["forecast"]

day = forecastday[0]

print(day["weekday"])