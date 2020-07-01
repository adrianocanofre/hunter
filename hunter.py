from bs4 import BeautifulSoup
import requests


URL = "https://www.pelando.com.br/recentes"

req = requests.get(URL)

soup = BeautifulSoup(req.content, 'html.parser')

for html in soup.find_all('div', class_="gridLayout-item"):
    h = html.find('strong', class_="thread-title")
    if h is not None:
        print(h.find('a').get_text())
    print('\n')
