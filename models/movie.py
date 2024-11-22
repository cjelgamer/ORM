from utils.db import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    duracion = db.Column(db.Integer)
    genero = db.Column(db.String(100))


    def __init__(self, nombre, duracion, genero):
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
