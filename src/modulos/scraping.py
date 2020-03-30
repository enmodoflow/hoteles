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

titulo = soup.find_all('h3', attrs={'class': 'c-h3--result highlight'})
print(titulo)



# for tag in tags:
#     print('URL:', tag.find())
#     print('Contents', tag.contents)
#     print('Attrs', tag.attrs)
#     print('\n')

# imagenes = soup('img')
# for i in imagenes:
#     print('IMG', i.get('src'))


# c = 0
# contenedor = soup.find('div', attrs={'class': 'contentCol'})

# img_contenedor = contenedor('h3')

# print(img_contenedor)
# for tag in img_contenedor:
#     print('TAG', tag)
#     print('URL:', tag.get('a'))
#     print('Contents', tag.contents)
#     print('Attrs', tag.attrs)
#     print('\n')

# tags = contenedor('li')
# for tag in contenedor:
#     print('TAG', tag)
    # print('URL:', tag.get('href'))
    # print('Contents', tag.contents)
    # print('Attrs', tag.attrs)
    # print('\n')




# imagenes = soup('img')
# for i in imagenes:
#     print(i.get('src'))

# busca por toda la página donde aparece esta unión de carácteres
# soup.findAll(text=re.compile('corona'))

# sacar enlaces con las palabras
# cantidad = soup.findAll('a')
# enlaces_corona = []
# palabras = ['coronavirus','Coronavirus','CORONAVIRUS', 'COVID-19', 'Covid-19','covid-19']
# for i in range(0, len(palabras)):
#     if soup.findAll('a', text=re.compile(palabras[i])):
#         enlaces_corona.append(soup.findAll('a', attrs={'href':re.compile('http')}, text=re.compile('coronavirus')))

# limpiar las url con http
# links = []
# for i in range(0, len(enlaces_corona)):
#     for link in enlaces_corona[i]:
#         links.append(link.get('href'))

# eliminar dublicados
# linksNuevo = set(links)

# links la lista con las url, necesarias para hacer un seguimiento de las noticias del coronavirus, en primera página del UltimaHora
# links = list(linksNuevo)

