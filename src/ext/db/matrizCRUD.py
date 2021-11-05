from ..site.model import Matriz
from ..site.model.Matriz import MatrizSchema
from ..db import db, ma

def cadastrarMatriz(matriz):  # Create
    try:
        if existsRFID(matriz.rfid):
            if existsNumero(matriz.numero):
                db.session.add(matriz)
                db.session.commit()
                return True
            else:
                return False
        else:
            return "RFID já cadastrado!"
    except BaseException as e:
        return False


def consultarMatrizes():  # Read
    try:
        matrizes = db.session.query(Matriz.Matriz).all()
        return matrizes
    except BaseException as e:
        return str(e)


def atualizarMatriz(request):  # Update
    try:
        matriz = db.session.query(Matriz.Matriz).filter_by(id=request.form.get("id")).first()
        matriz.quantidade = request.form.get("quantidade")
        db.session.commit()
        return True
    except BaseException as e:
        return False


def excluirMatriz(id):  # Delete
    try:
        matriz = db.session.query(Matriz.Matriz).filter_by(id=id).first()
        db.session.delete(matriz)
        db.session.commit()
        return True
    except BaseException as e:
        return False
    
def consultarMatriz(id):  # Read
    try:
        matriz = db.session.query(Matriz.Matriz).filter_by(id=id).first()
        if not matriz:
            raise Exception("")
        matriz_schema = MatrizSchema()
        return MatrizSchema().dump(matriz)
    except Exception as e:
        return e.args[0]
    
def consultarMatrizRFID(rfid):  # Read
    try:
        matriz = db.session.query(Matriz.Matriz).filter_by(rfid=rfid).first()
        return matriz
    except:
        return False
    
def existsRFID(rfid):
    exists = db.session.query(db.exists().where(Matriz.Matriz.rfid == rfid)).scalar()
    if exists:
        return False
    else:
        return True
    
def existsNumero(numero):
    exists = db.session.query(db.exists().where(Matriz.Matriz.numero == numero)).scalar()
    print(str(exists))
    if exists:
        return False
    else:
        return True
    
def consultarMatrizID(rfid):  # Read
    try:
        matriz = db.session.query(Matriz.Matriz.id).filter_by(rfid=rfid).first()
        a = str(matriz).replace(", )", "")
        id = str(a).replace("(", "")
        return matriz[0]
    except:
        return False