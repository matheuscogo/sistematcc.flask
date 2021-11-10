from ext.db import confinamentoCRUD
from ...db import db
from flask_restx import Api, Namespace, Resource, fields, reqparse
from ext.site.model import Confinamento
from ext.site.model.Confinamento import ConfinamentoSchema
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import NotFound
from werkzeug.exceptions import InternalServerError

namespace = Namespace('Confinamentos', description='Confinamentos', path='/confinamentos')

insert_confinamento = namespace.model('Dados para criação de Matrizes', {
    'dataConfinamento': fields.String(required=True, description='Data de entrada no confinamento'),
    'matriz': fields.Integer(required=True, description='FK da matriz'),
    'plano': fields.Integer(required=True, description='FK do plano de alimentação')
})

update_confinamento = namespace.model('Dados para atualizar o confinamento', {
    'id': fields.Integer(required=True, description='ID do confinamento'),
    'dataConfinamento': fields.String(required=True, description='Data de /entrada no confinamento'),
    'matriz': fields.Integer(required=True, description='FK da matriz'),
    'plano': fields.Integer(required=True, description='FK do plano de alimentação')
})

list_confinamento = namespace.model('Lista de confinamentos', {
    'id': fields.Integer(required=True, description='ID do confinamento'),
    'dataConfinamento': fields.String(required=True, description='Data de /entrada no confinamento'),
    'matriz': fields.Integer(required=True, description='FK da matriz'),
    'plano': fields.Integer(required=True, description='FK do plano de alimentação')
})

list_confinamento_response = namespace.model('Resposta para lista de confinamentos', {
    'data': fields.Nested(list_confinamento, required=True, description='Lista de confinamentos')
})

headers = namespace.parser()

@namespace.route('/insert')
@namespace.expect(headers)
class CreateConfinamento(Resource):
    @namespace.expect(insert_confinamento, validate=True)
    def post(self):
        """Cadastra um confinamento"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('dataConfinamento', type=str)
            parser.add_argument('matriz', type=int)
            parser.add_argument('plano', type=int)
            args = parser.parse_args()
            confinamento = confinamentoCRUD.cadastrarConfinamento(args)
            if not confinamento:
                raise Exception("Error")
            return confinamento
        except Exception as e:
            raise InternalServerError(e.args[0])

@namespace.route('/update/')
@namespace.expect(headers)
class UpdateRegistro(Resource):
    @namespace.expect(update_confinamento, validate=True)
    def put(self):
        """Atualiza um confinamento"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=int)
            parser.add_argument('dataConfinamento', type=str)
            parser.add_argument('matriz', type=int)
            parser.add_argument('plano', type=int)
            args = parser.parse_args()
            confinamento = confinamentoCRUD.atualizarConfinamento(args)
            if not confinamento:
                raise Exception("Error")
            return confinamento
        except Exception as e:
            raise InternalServerError(e.args[0])

@namespace.route('/<int:id>')
@namespace.param('id')
@namespace.expect(headers)
class GetRegistro(Resource):
    def get(self, id):
        """Consulta um registro por id"""
        try:
            confinamento = confinamentoCRUD.consultarConfinamento(id)
            return confinamento
        except HTTPException as e:
            raise InternalServerError(e.args[0])


@namespace.route('/')
@namespace.expect(headers)
class ListaRegistros(Resource):
    @namespace.marshal_with(list_confinamento_response)
    def get(self):
        """Lista todos os confinamentos"""
        try:
            confinamentos = confinamentoCRUD.consultarConfinamentos()
            if not confinamentos:
                raise BaseException("Erro ao consultar no banco de dados")
            return {"data": confinamentos}
        except HTTPException as e:
            raise InternalServerError(e.args[0])


@namespace.route('/delete/<int:id>')
@namespace.param('id', 'ID do confinamento')
@namespace.expect(headers)
class DeleteRegistro(Resource):
    def delete(self, id):
        """Remove um registro"""
        try:
            confinamento = confinamentoCRUD.excluirConfinamento(id)
            return confinamento
        except Exception as e:
            raise InternalServerError(e.args[0])

def bind_with_api(api: Api):
    api.add_namespace(namespace)
    return None