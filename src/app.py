import unittest
import os
from flask import Flask


# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def home():
    print("Hola mundo")
    return '¡Hola, mundo! Esta es mi primera aplicación Flask.'

# Ruta para una página de ejemplo
@app.route('/pagina-ejemplo')
def pagina_ejemplo():
    print("pagina ejemplo")
    return 'Esta es una página de ejemplo.'

# Ruta dinámica con parámetro
@app.route('/saludo/<nombre>')
def saludo(nombre):
    return '¡Hola, {}!'.format(nombre)

# Ejecuta la aplicación Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
