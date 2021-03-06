from ext.site.model.Inseminacao import Inseminacao, InseminacaoSchema
from ...db import db, inseminacaoCRUD
from flask_restx import Api, Namespace, Resource, fields, reqparse
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import NotFound
from werkzeug.exceptions import InternalServerError

namespace = Namespace(name='Inseminação', description='Inseminação', path='/inseminacao')

insert_inseminacao = namespace.model('Dados para criação de uma inseminação', {
    'matrizId': fields.Integer(required=True, description='ID da inseminação'),
    'planoId': fields.Integer(required=True, description='Plano para inseminação'),
    'dataInseminacao': fields.Integer(required=True, description='Data da inseminação'),
    'isNewCiclo': fields.Boolean(required=True, description='isNewCiclo')
})

update_inseminacao = namespace.model('Dados para atualização de inseminações', {
    'id': fields.Integer(required=True, description='ID da inseminação'),
    'matrizId': fields.Integer(required=True, description='ID da inseminação'),
    'planoId': fields.Integer(required=True, description='Plano para inseminação'),
    'dataInseminacao': fields.String(required=True, description='Data da inseminação'),
})

list_inseminacoes = namespace.model('Lista de inseminacaoes', {
    'id': fields.String(required=True, description='Identificadores das inseminacaoes'),
    'matrizDescription': fields.String(required=True, description='ID da inseminação'),
    'planoDescription': fields.String(required=True, description='Plano para inseminação'),
    'dataInseminacao': fields.String(required=True, description='Data da inseminação')    
})

list_inseminacaoes_response = namespace.model('Resposta da lista de inseminacaoes', {
    'data': fields.Nested(list_inseminacoes, required=True, description='Lista de inseminações')
})

delete_episode_response = namespace.model('Resposta da remocao de inseminacaoes', {
    'removed': fields.Boolean(required=True, description='Indicador de remocao com sucesso')
})

headers = namespace.parser()
# Aqui podemos adicionar mais parametros ao headers

@namespace.route('/insert', methods=['POST'])
@namespace.expect(headers)
class CreateInseminacao(Resource):
    @namespace.expect(insert_inseminacao, validate=True)
    @namespace.doc(security='apikey')
    def post(self):
        """Cadastra uma inseminação"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('matrizId', type=int)
            parser.add_argument('planoId', type=int)
            parser.add_argument('dataInseminacao', type=int)
            parser.add_argument('isNewCiclo', type=bool)
            args = parser.parse_args()
            inseminacao = inseminacaoCRUD.cadastrarInseminacao(args)
            if not inseminacao:
                raise Exception("Error")
            return inseminacao
        except Exception as e:
            raise InternalServerError(e.args[0])

@namespace.route('/update/', methods=["PUT"])
@namespace.expect(headers)
class UpdateInseminacao(Resource):
    @namespace.expect(update_inseminacao, validate=True)
    def put(self):
        """Atualiza uma inseminação"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=int)
            parser.add_argument('matrizId', type=int)
            parser.add_argument('dataInseminacao', type=str)
            args = parser.parse_args()
            inseminacao = inseminacaoCRUD.atualizarInseminacao(args)
            if not inseminacao:
                raise Exception("Error")
            return inseminacao
        except Exception as e:
            raise InternalServerError(e.args[0])

@namespace.route('/<int:id>', methods=["GET"])
@namespace.param('id')
@namespace.expect(headers)
class GetInseminacao(Resource):
    def get(self, id):
        """Consulta uma inseminação por id"""
        try:
            inseminacao = inseminacaoCRUD.consultarInseminacao(id)
            return inseminacao
        except HTTPException as e:
            raise InternalServerError(e.args[0])


@namespace.route('/', doc={"description": 'Lista todos os inseminações'}, methods=["GET"])
@namespace.expect(headers)
class ListaInseminacoes(Resource):
    @namespace.marshal_with(list_inseminacaoes_response)
    def get(self):
        """Lista todos os inseminações"""
        try:
            inseminacaoes = inseminacaoCRUD.consultarInseminacoes()
            return {"data": inseminacaoes}
        except HTTPException as e:
            raise InternalServerError(e.args[0])


@namespace.route('/delete/<int:id>',
                 doc={"description": 'Apaga inseminacaoes'},
                 methods=['DELETE'])
@namespace.param('id', 'ID da inseminacao')
@namespace.expect(headers)
class DeleteInseminacao(Resource):
    def delete(self, id):
        """Remove inseminação"""
        try:
            inseminacao = inseminacaoCRUD.excluirInseminacao(id)
            return inseminacao
        except Exception as e:
            raise InternalServerError(e.args[0])

def bind_with_api(api: Api):
    """
    Adiciona o namespace à API recebida
    :param api: Flask Restplus API
    :return: Vazio
    """
    api.add_namespace(namespace)
    return None