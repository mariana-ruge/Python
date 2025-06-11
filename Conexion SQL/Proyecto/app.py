#Importar flask
from flask import Flask, jsonify
#Importar del modelo
from model import db, Streamers
from logging import exception

#Crear una instancia de la aplicación
app = Flask(__name__)
#Configurar la aplicacion
#Configurar la base de datos con SQL Alchemy
app.config["SQLALCHEMY_DATABASE_URI"] = r"sqlite:///C:\Users\maria\OneDrive\Escritorio\Códigos\Python\Conexion SQL\streamers.db"
app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False

#Conectar la base de datos
db.init_app(app)

#Crear el decorador
@app.route("/")

#Función que se ejecuta al acceder a la ruta
def home():
    return "<h1> Welcome home </h1>"

@app.route("/api/streamers")
#Función que obtiene los stremaer
def getStreamers():
    try:
        streamers = Streamers.query.all()
        #Guardar objeto streamer
        #Generar una comprehension list
        toReturn = [streamer.serialize() for streamer in streamers]
        #Generar una respuesta de tipo json
        return jsonify(toReturn), 200
            
    except Exception:
        print("Algo ha salido mal")
        exception("[SERVER]: Error -> ")
        return jsonify({"msg": "Ha ocurrido un error"}), 500
    
    return "<h1> Success </h1>"

#Entry point
if __name__ == "__main__":
    app.run(debug=True, port=4000)