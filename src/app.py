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

# Iniciando FLASK
app = Flask(__name__)
app.secret_key = 'E86xBi9k!y'

# RUTAS 
@app.route('/', methods=['GET', 'POST'])
def inicio():
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run("0.0.0.0", port=port, debug=True)