import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.wallpaperflare.com/")
data = BeautifulSoup(response.content, 'html.parser')
# print(data.prettify())

for x in data.find_all('img', attrs={'class': 'lazy'}):
    print("Description: " + x['alt'] + "\nLink: " + x['data-src'] + "\n")
