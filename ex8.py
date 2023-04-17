import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
resposta = requests.get(url)

html = resposta.text
soup = BeautifulSoup(html, 'html.parser')

titulos = soup.find_all('h2')

for titulo in titulos:
    print(titulo.text.strip())