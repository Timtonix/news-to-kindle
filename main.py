import requests
from bs4 import BeautifulSoup
import sqlite3


r = requests.get('https://www.courrierinternational.com/magazine')

# Creation de l'objet à analyser
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify().strip())

for article in soup.find_all('article'):
    print(article)

