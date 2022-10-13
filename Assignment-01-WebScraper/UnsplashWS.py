import requests
from bs4 import BeautifulSoup

response = requests.get("https://unsplash.com/")
data = BeautifulSoup(response.content, 'html.parser')
# print(root.prettify())

for x in data.find_all('img', attrs={'class': 'YVj9w'}):
    print(x['src'] + "\n")
    # print(x)
