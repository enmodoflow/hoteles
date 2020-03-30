# Flask
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from pymongo import MongoClient
import modulos.mongo as mongo
import os


# Iniciando FLASK
app = Flask(__name__)
app.secret_key = 'Quedate en tu casa que mira que es facil'


# RUTAS 
@app.route('/', methods=['GET', 'POST'])
def inicio():
    busqueda = list(mongo.collection.find({}))
    lista = []
    for i in busqueda:
        lista.append([i['titulo'], i['descripcion'], i['alquiler'], i['precio'], i['img']])
    return render_template('index.html', lista=lista)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run("0.0.0.0", port=port, debug=True)