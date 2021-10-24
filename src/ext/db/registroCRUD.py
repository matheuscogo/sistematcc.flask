from ..db import db
from ..site.model import Registro


def cadastrarRegistro(registro):  # Create
    try:
        db.session.add(registro)
        db.session.commit()
        return True
    except BaseException as e:
        return False

def consultarRegistros():  # Read
    try:
        registros = db.session.query(Registro.Registro).all()
        return registros
    except BaseException as e:
        return "False"

def atualizarRegistro(registro):  # Update
    db.session.add()


def excluirRegistro(registro):  # Delete
    db.session.add()

def consultarRegistro(id):
    try:
        registros = db.session.query(Registro.Registro).filter_by(matriz=id).all()
        for registro in registros:
            print(registro)
        return registros
    except:
        return False