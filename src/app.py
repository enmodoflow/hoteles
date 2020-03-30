# Flask
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

# modulo Scraping
import modulos.scraping as scrap
# modulo Base de datos
import modulos.mongodb as mongo

# Python
import os

# Mongo
from pymongo import MongoClient

# Iniciando FLASK
app = Flask(__name__)
app.secret_key = 'Quedate en tu casa que mira que es facil'



# RUTAS 
@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        mongo.collection.insert_one({'nombre': nombre})
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run("0.0.0.0", port=port, debug=True)