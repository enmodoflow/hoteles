# Scraping
from bs4 import BeautifulSoup
import requests
import lxml
import urllib
import re

# Mongodb
from pymongo import MongoClient

# Mongo URL Atlas
MONGO_URL_ATLAS = 'mongodb+srv://lolo:root@cluster0-nqj9e.mongodb.net/test?retryWrites=true&w=majority'

client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs=False)
db = client['examen_final']
collection = db['examen_final']

# Objetivo
url = "https://www.escapadarural.com/casas-rurales-aisladas"
# Recogida de HTML
hoteles = requests.get(url)

# VAMOS A EMPEZAR A PREPARAR LA 'SOUP'
soup = BeautifulSoup(hoteles.text, 'lxml')

diccionario = {}


# sacar todos los elementos del scrapping, y irlos metiendo en un diccionario
c = 0
titulo = soup.find_all('a', attrs={'class': 'c-result--link'})
for i in titulo:
    if c < 3:
        diccionario['titulo'+ str(c)] = i.contents
        c +=1

co = 0
descripcion = soup.find_all('div', attrs={'class': 'c-result--abstract'})
for i in descripcion:
    if co < 3:
        diccionario['descripcion'+ str(co)] = i.find('p').contents
        co += 1

con = 0        
alquiler = soup.find_all('div', attrs={'class': 'c-result--item--text'})
for i in alquiler:
    if con < 3:
        diccionario['alquiler'+ str(con)] = i.contents
        con += 1

cont = 0
precio = soup.find_all('div', attrs={'class': 'c-price--average'})
for i in precio:
    if cont < 3:
        diccionario['precio'+ str(cont)] = i.contents[0]
        cont += 1


# insertar recogida de datos en un diccionario
collection.insert_one(diccionario)


