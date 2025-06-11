#Importar la clase SQl Alchemy
from flask_sqlalchemy import SQLAlchemy

#Recrear la tabla de estreamers

db = SQLAlchemy()

class Streamers(db.Model):
    __tablename__ = "streamers_actualizado" 
    #Primary Key
    rowid = db.Column(db.Integer, primary_key = True)
    #Filas y columnas
    name = db.Column(db.String(200), unique=True, nullable=False)
    subs = db.Column(db.Integer)
    followers = db.Column(db.Integer)
    
    def __repr__(self):
        return "\nNombre: {}. Subs{}. Followers {}.".format(
            self.name,
            self.subs,
            self.followers
        )
    
    #Serializar los datos
    def serialize(self):
        return{
            "rowid": self.rowid,
            "name": self.name,
            "subs": self.subs,
            "followers": self.followers
        }