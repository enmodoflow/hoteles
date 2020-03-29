# Scraping
from bs4 import BeautifulSoup
import requests
import lxml

import re

# Objetivo
url = "https://www.diariodemallorca.es"
# Recogida de HTML
diariomallorca = requests.get(url)

# VAMOS A EMPEZAR A PREPARAR LA 'SOUP'
soup = BeautifulSoup(diariomallorca.text, 'lxml')

# busca por toda la página donde aparece esta unión de carácteres
soup.findAll(text=re.compile('corona'))

# sacar enlaces con las palabras
cantidad = soup.findAll('a')
enlaces_corona = []
palabras = ['coronavirus','Coronavirus','CORONAVIRUS', 'COVID-19', 'Covid-19','covid-19']
for i in range(0, len(palabras)):
    if soup.findAll('a', text=re.compile(palabras[i])):
        enlaces_corona.append(soup.findAll('a', attrs={'href':re.compile('http')}, text=re.compile('coronavirus')))

# limpiar las url con http
links = []
for i in range(0, len(enlaces_corona)):
    for link in enlaces_corona[i]:
        links.append(link.get('href'))

# eliminar dublicados
linksNuevo = set(links)

# links la lista con las url, necesarias para hacer un seguimiento de las noticias del coronavirus, en primera página del UltimaHora
links = list(linksNuevo)