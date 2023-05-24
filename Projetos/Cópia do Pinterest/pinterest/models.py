from pinterest import database
from datetime import datetime

class Usuario(database.model):
    id = database.Column(database.Integer, primary_key = True)
    username = database.Column(database.String, nullabe = False)
    email = database.Column(database.String, nullabe = False, unique = True)
    senha = database.Column(database.String, nullabe = False)
    fotos =database.relationship("Foto", backref = "usuario", lazy = True)

class Foto(database.model):
    id = database.Column(database.Integer, primary_key = True)
    imagem = database.Column(database.String, default = "default.png")
    data_criacao = database.Column(database.DateTime, nullabe = False, default=datetime.utcnow())
    id_usuario = database.relationship(database.Integer,database.ForeifnKey("usuaio.id"), nullabe = False, )