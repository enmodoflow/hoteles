# Scraping
from bs4 import BeautifulSoup
import requests
import lxml
import urllib
import re

# Objetivo
url = "https://www.escapadarural.com/casas-rurales-aisladas"
# Recogida de HTML
hoteles = requests.get(url)

# VAMOS A EMPEZAR A PREPARAR LA 'SOUP'
soup = BeautifulSoup(hoteles.text, 'lxml')


# contenedor = soup.find('div', attrs={'class': 'contentCol'})

# titulo = soup.find_all('a', attrs={'class': 'c-result--link'})
# for i in titulo:
#     print(i.contents)

# descripcion = soup.find_all('div', attrs={'class': 'c-result--abstract'})
# for i in descripcion:
#     print(i.find('p').contents)

# alquiler = soup.find_all('div', attrs={'class': 'c-result--item--text'})
# for i in alquiler:
#     print(i.contents)

link = soup.find_all('article', attrs={'class': 'c-resultSnippet JS_resultSnippet'})
for i in link:
    print(i.find('rel'))


# precio = soup.find_all('div', attrs={'class': 'c-price--average'})
# for i in precio:
#     print(i.contents[0])


