import os
from flask import Flask
import pandas


app = Flask(__name__)



# Metodo que ejecuta toda la carga de la base de datos
@app.route('/prueba', methods=['GET'])
def prueba():
    print("Llego la petición !!!")
    return "Se ejecuta el proceso de prueba"




# Ejecuta la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
