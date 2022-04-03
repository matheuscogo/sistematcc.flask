from queue import Empty

from responses import activate, delete
from ..site.model import Confinamento
from ..site.model.Confinamento import ConfinamentoSchema
from ..db import db
import datetime
from werkzeug.wrappers import Response, Request
from xmlrpc.client import ResponseError
import json
from ..site.model import Dia
from ..site.model.Plano import Plano
from ..site.model.Matriz import Matriz
from ..site.model.Registro import Registro
from ..db import db
from sqlalchemy.sql import func
from datetime import datetime, timedelta


def cadastrarConfinamento(args):  # Create
    try:
        dataConfinamento = int(args['dataConfinamento'])
        matrizId = int(args['matrizId'])
        planoId = int(args['planoId'])

        dataConfinamento = datetime.strftime(datetime.fromtimestamp(dataConfinamento/1000.0), '%d/%m/%y')

        if not matrizId:
            raise Exception(ResponseError)

        if not planoId:
            raise Exception(ResponseError)
            
        if not dataConfinamento:
            raise Exception(ResponseError)

        confinamento = db.session.query(Confinamento.Confinamento).filter_by(matrizId=matrizId, deleted=False, active=True).first()

        if confinamento:
            confinamento.active = False
            confinamento.deleted = True

        db.session.add(Confinamento.Confinamento(
            planoId=planoId,
            matrizId=matrizId,
            dataConfinamento=dataConfinamento)
        )

        db.session.commit()
        return Response(response=json.dumps("{success: true, message: Confinamento cadastrado com sucesso!, response: null}"), status=200)
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)


def consultarConfinamento(id):  # Read
    try:
        confinamento = db.session.query(Confinamento).filter_by(id=id, active=True, deleted=False).first()
        return ConfinamentoSchema().dump(confinamento)
    except BaseException as e:
        return str(e)

def consultarConfinamentos():  # Read
    try:
        response = db.session.query(Confinamento.Confinamento).filter_by(deleted=False, active=True).all()
        
        confinamentos = []

        for confinamento in response:
            matrizDescription = db.session.query(Matriz).filter_by(id=int(confinamento.matrizId), deleted=False).first()
            planoDescription = db.session.query(Plano).filter_by(id=int(confinamento.planoId), active=True, deleted=False).first()
            obj = {"id": confinamento.id, "planoDescription": planoDescription.nome, "matrizDescription": matrizDescription.rfid, "dataConfinamento": confinamento.dataConfinamento}
            confinamentos.append(obj)
            
        return confinamentos
    except BaseException as e:
        return str(e)

def atualizarConfinamento(args):
    try:
        id = args['id']
        dataConfinamento = args['dataConfinamento']
        plano = args['plano']
        matriz = args['matriz']
        confinamento = db.session.query(Confinamento).filter_by(id=id).first()
        confinamento.dataConfinamento = dataConfinamento
        confinamento.matriz = matriz
        confinamento.plano = plano
        db.session.commit()
        return Response(response=json.dumps("{success: true, message: Confinamento atualizado com sucesso!, response: null}"), status=200)
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)

def excluirConfinamento(id):  # Delete
    try:
        confinameto = db.session.query(Confinamento).filter_by(id=id).first()
        db.session.delete(confinameto)
        db.session.commit()
        return Response(response=json.dumps("{success: true, message: Confinameto excluido com sucesso!, response: null}"), status=200)
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: "+ e.args[0] +", response: null}"), status=501)


def getConfinamentoByMatriz(matrizId):
    try:
        confinamento = db.session.query(Confinamento.Confinamento).filter_by(matrizId=matrizId, active=True, deleted=False).first()
        return ConfinamentoSchema().dump(confinamento)
    except BaseException as e:
        return str(e)


def getQuantityForMatriz(matrizId):
    try:
        confinamento = db.session.query(Confinamento).filter_by(matrizId=matrizId, deleted=False, active=True).first()
        matrizId = confinamento['matrizId']
        planoId = confinamento['planoId']
        dataEntrada = confinamento['dataConfinamento']
        
        day = getDaysInConfinament(matrizId=matrizId)
        dayQuantity = db.session.query(Dia.Dias.quantidade).filter_by(planoId=planoId, dia=day).first()
        totalQuantity = db.session.query(func.sum(Registro.Registro.quantidade)).filter_by(matriz=matrizId, dataEntrada=dataEntrada).first()[0]
        
        total = totalQuantity - dayQuantity
        return total
    except BaseException as e:
        return e.args[0]


def verifyDaysToOpen(matrizId):
    try:
        day = getDaysInConfinament(matrizId=matrizId)
        
        # paramters = getParameters
        
        if day >= 110:
            return True
        else:
            return False
    except BaseException as e:
        return e.args[0]


def getDaysInConfinament(matrizId):
    confinamento = db.session.query(Confinamento).filter_by(matrizId=matrizId, deleted=False, active=True).first()
    dataEntrada = datetime.datetime.strptime(confinamento['dataConfinamento'], '%d/%m/%y')
    dataAtual = datetime.datetime.today()
    days = dataAtual - timedelta(dataEntrada)
    print("DIA ENTRADA = " + str(dataEntrada))
    print("DIA ATUAL = " + str(dataAtual))
    return days
