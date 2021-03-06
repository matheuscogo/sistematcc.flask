from ..site.model import Registro
from ..site.model.Registro import RegistroSchema
from ..db import db
from werkzeug.wrappers import Response, Request
from datetime import datetime
import json


def cadastrarRegistro(args):  # Create
    try:
        matrizId = args['matrizId']
        dataEntrada = args['dataEntrada']
        dataSaida = args['dataSaida']
        horaEntrada = args['horaEntrada']
        horaSaida = args['horaSaida']
        tempo = args['tempo']
        quantidade = args['quantidade']
        
        dataEntrada = datetime.strftime(datetime.fromtimestamp(dataEntrada/1000.0), '%d/%m/%y')
        dataSaida = datetime.strftime(datetime.fromtimestamp(dataSaida/1000.0), '%d/%m/%y')
        horaEntrada = datetime.strftime(datetime.fromtimestamp(horaEntrada/1000.0), 'HH:mm:ss')
        horaSaida = datetime.strftime(datetime.fromtimestamp(horaSaida/1000.0), 'HH:mm:ss')
        
        tempo = datetime.strftime(datetime.fromtimestamp(tempo/1000.0), '%d/%m/%y')
        
        db.session.add(Registro.Registro(
            matriz=matrizId,
            dataEntrada=dataEntrada,
            dataSaida=dataSaida,
            horaEntrada=horaEntrada,
            horaSaida=horaSaida,
            tempo=tempo,
            quantidade=quantidade
        ))
        db.session.commit()
        return Response(response=json.dumps("{success: true, message: Registro cadastrado com sucesso!, response: null}"), status=200)
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)


def consultarRegistros():  # Read
    try:
        registros = db.session.query(Registro.Registro).all()
        if not registros:
            raise BaseException("Erro ao consultar no banco de dados")
        return registros
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)


def consultarRegistro(id): # Read
    try:
        registro = db.session.query(Registro.Registro).filter_by(id=id).first()
        if not registro:
            raise BaseException("Erro ao cadastrar no banco")
        return  RegistroSchema().dump(registro)
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)


def atualizarRegistro(args):  # Update
    try:
        id = int(args['id'])
        matriz = int(args['matriz'])
        dataEntrada = str(args['dataEntrada'])
        dataSaida = str(args['dataSaida'])
        horaEntrada = str(args['horaEntrada'])
        horaSaida = str(args['horaSaida'])
        tempo = str(args['tempo'])
        quantidade = int(args['quantidade'])

        registro = db.session.query(Registro.Registro).filter_by(id=id).first()
        registro.matriz = matriz
        registro.dataEntrada = dataEntrada
        registro.dataSaida = dataSaida
        registro.horaEntrada = horaEntrada
        registro.horaSaida = horaSaida
        registro.tempo = tempo
        registro.quantidade = quantidade
        db.session.commit()
        return Response(response=json.dumps("{success: true, message: Registro atualizado com sucesso!, response: null}"), status=200)
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)


def excluirRegistro(id):  # Delete
    try:
        registro = db.session.query(Registro.Registro).filter_by(id=id).first()
        db.session.delete(registro)
        db.session.commit()
        return Response(response=json.dumps("{success: true, message: Registro excluido com sucesso!, response: null}"), status=200)
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: "+ e.args[0] +", response: null}"), status=501)
