from ..site.model import Plano, Dias
from ..db import db
import json


def cadastrarPlano(plano, json_str):  # Create
    try:
        if exists(plano.nome):
            db.session.add(plano)
            db.session.commit()
            json_list = list(json.loads(json_str)['plano'])
            for dados in json_list:
                dias = list(dados["dias"])
                quantidade = list()
                quantidade.append(dados["quantidade"])
                cont = 0
                for cont in range(dias[0], dias[1] + 1):
                    print("TO NO CADASTRA PLANO NO CRUD")
                    print("Dia " + str(cont) + ": " +
                      str(cont) + " -> " + str(quantidade[0]))
                    db.session.add(Dias.Dias(plano=int(db.session.query(Plano.Plano.id).filter_by(
                        nome=plano.nome).first()[0]), dia=int(cont), quantidade=int(quantidade[0])))
                    db.session.commit()
                    cont = cont + 1
            return ""
        else:
            return ""
    except BaseException as e:
        return "Deu erro no crud"


def consultarPlanos():  # Read
    try:
        plano = db.session.query(Plano.Plano).all()
        return plano
    except BaseException as e:
        return False


def atualizarPlano(request):  # Update
    try:
        matriz = db.session.query(Plano.Plano).filter_by(
            id=request.form.get("id")).first()
        matriz.quantidade = request.form.get("quantidade")
        db.session.commit()
        return True
    except BaseException as e:
        return False


def excluirPlano(plano):  # Delete
    try:
        plano = db.session.query(Plano.Plano).filter_by(id=plano).first()
        db.session.delete(plano)
        db.session.commit()
        return True
    except BaseException as e:
        return False


def exists(nome):
    exists = db.session.query(db.exists().where(
        Plano.Plano.nome == nome)).scalar()
    print(str(exists))
    if exists:
        return False
    else:
        return True


def consultarPlano(id):
    try:
        plano = db.session.query(Plano.Plano).filter_by(id=id).first()
        return plano
    except:
        return False


def consultarDias():  # Read
    try:
        dias = db.session.query(Dias.Dias).all()
        return dias
    except BaseException as e:
        return False


def atualizarDias(request):  # Update
    try:
        matriz = db.session.query(Plano.Plano).filter_by(
            id=request.form.get("id")).first()
        matriz.quantidade = request.form.get("quantidade")
        db.session.commit()
        return True
    except BaseException as e:
        return False


def excluirDia(plano):  # Delete
    try:
        plano = db.session.query(Plano.Plano).filter_by(id=plano).first()
        db.session.delete(plano)
        db.session.commit()
        return True
    except BaseException as e:
        return False


def exists(nome):
    exists = db.session.query(db.exists().where(
        Plano.Plano.nome == nome)).scalar()
    print(str(exists))
    if exists:
        return False
    else:
        return True


def consultarDia(id):
    try:
        dia = db.session.query(Dias.Dias).filter_by(plano=id).all()
        return dia
    except:
        return False


def consultarQuantidade(id):
    try:
        quantidades = db.session.query(
            Dias.Dias.quantidade).filter_by(plano=id).all()
        array = list()
        for quantidade in quantidades:
            array.append(quantidade[0])
        json_str = json.dumps(array)
        return json_str
    except:
        return False
