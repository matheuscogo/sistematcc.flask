from ..site.model import Plano, Dias
from ..site.model.Plano import PlanoSchema
from ..db import db
from werkzeug.wrappers import Response, Request
import json

def cadastrarPlano(args):  # Create
    try:
        nome = args['nome']
        descricao = args['descricao']
        tipo = args['tipo']
        quantidadeDias = args['quantidadeDias']
        ativo = True
        db.session.add(Plano.Plano(
            nome=nome,
            descricao=descricao,
            tipo=tipo,
            quantidadeDias=quantidadeDias,
            ativo=ativo)
        )
        db.session.commit()
        return Response(response=json.dumps("{success: true, message: Plano cadastrado com sucesso!, response: null}"), status=200)
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)


def consultarPlanos():  # Read
    try:
        planos = db.session.query(Plano.Plano).all()
        return planos
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)
    
def consultarPlano(id): # Read
    try:
        plano = db.session.query(Plano.Plano).filter_by(id=id).first()
        return PlanoSchema().dump(plano)
    except Exception as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)

def atualizarPlano(args):  # Update
    try:
        id = int(args['id'])
        nome = str(args['nome'])
        descricao = str(args['descricao'])
        tipo = int(args['tipo'])
        quantidadeDias = int(args['quantidadeDias'])
        ativo = args['ativo']

        if(ativo == "true"):
            ativo = True
        else:
            ativo = False
        
        plano = db.session.query(Plano.Plano).filter_by(id=id).first()
        plano.nome = nome
        plano.descricao = descricao
        plano.tipo = tipo
        plano.quantidadeDias = quantidadeDias
        plano.ativo = ativo
        db.session.commit()
        return Response(response=json.dumps("{success: true, message: Plano atualizado com sucesso!, response: null}"), status=200)
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)


def excluirPlano(id):  # Delete
    try:
        plano = db.session.query(Plano.Plano).filter_by(id=id).first()
        db.session.delete(plano)
        db.session.commit()
        return Response(response=json.dumps("{success: true, message: Plano excluido com sucesso!, response: null}"), status=200)
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: "+ e.args[0] +", response: null}"), status=501)

def exists(nome):
    exists = db.session.query(db.exists().where(
        Plano.Plano.nome == nome)).scalar()
    print(str(exists))
    if exists:
        return False
    else:
        return True

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
