from ..site.model.Confinamento import association_table
from ..site.model import Dias
from ..site.model import Plano
from ..site.model import Matriz
from ..site.model import Registro
from ..db import db
from sqlalchemy.sql import func
import datetime


def cadastrarConfinamento(request):  # Create
    try:
        dataEntrada = str(request.form.get("dataEntrada"))
        matriz = int(request.form.get("matriz"))
        plano = int(request.form.get("plano"))
        db.session.execute(association_table.insert().values(
            matriz=matriz, plano=plano, dataEntrada=dataEntrada))
        db.session.commit()
        return True
    except BaseException as e:
        return False


def consultarConfinamento(rfid):  # Read
    try:
        matriz = db.session.query(
            Matriz.Matriz.id).filter_by(rfid=rfid).first()[0]
        confinamento = db.session.query(
            association_table).filter_by(matriz=matriz).all()[0]
        return confinamento
    except BaseException as e:
        return str(e)


def consultarQuantidade(rfid, dataEntrada):
    confinamento = consultarConfinamento(rfid)
    matriz = confinamento[0]
    plano = confinamento[1]
    dataConfinamento = confinamento[2]
    dia1 = converteData(dataConfinamento)
    dia2 = converteData(dataEntrada)
    dia = (dia2 - dia1).days
    print("--------------------")
    print()
    print("DIA 1 = " + str(dia1))
    print("DIA 2 = " + str(dia2))
    print("Quantidade de dias no confinamento = " + str(dia))
    stmt = """SELECT d.quantidade
              FROM dias d, planos p
              WHERE p.id = d.plano
              AND p.id = """ + str(plano) + """
              AND d.dia = """ + str(dia)
    quantidade = db.session.execute(stmt).first()[0]
    total = db.session.query(func.sum(Registro.Registro.quantidade)).filter_by(matriz=matriz, dataEntrada=dataEntrada).first()[0]
    if dia >= 27:
        print("ABRIR PORTA")
    else:
        print("Não está em tempo ainda")
    if total is None:
        total = quantidade
    else:
        total = quantidade - total
    print("Total de ração do dia = " + str(total))
    print()
    print("--------------------")
    dia = 0
    return total


def consultarUltimaEntrada(matriz):
    dia2 = """SELECT MAX(r.dataEntrada) as dia
              FROM registros r, confinamento c
              WHERE r.matriz = c.matriz
              AND c.matriz = """ + str(matriz)
    dia2 = db.session.execute(dia2).first()[0]
    return dia2


def converteData(dataEntrada):
    data = datetime.datetime.strptime(dataEntrada, "%Y-%m-%d")
    return data


def atualizarMatriz(request):  # Update
    try:
        matriz = db.session.query(Matriz.Matriz).filter_by(
            id=request.form.get("id")).first()
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
        return matriz
    except:
        return False


def consultarMatrizRFID(rfid):  # Read
    try:
        matriz = db.session.query(Matriz.Matriz).filter_by(rfid=rfid).first()
        return matriz
    except:
        return False


def existsMatriz(rfid):
    exists = db.session.query(db.exists().where(
        Matriz.Matriz.rfid == rfid)).scalar()
    print(str(exists))
    if exists:
        return False
    else:
        return True


def existsPlano(numero):
    exists = db.session.query(db.exists().where(
        Matriz.Matriz.numero == numero)).scalar()
    print(str(exists))
    if exists:
        return False
    else:
        return True


# def consultarQuantidade(id):
#     try:
#         quantidades = db.session.query(
#             Dias.Dias.quantidade).filter_by(plano=id).all()
#         array = list()
#         for quantidade in quantidades:
#             array.append(quantidade[0])
#         json_str = json.dumps(array)
#         return json_str
#     except:
#         return False
