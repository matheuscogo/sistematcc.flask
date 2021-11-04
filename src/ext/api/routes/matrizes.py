from ...db import db, matrizCRUD
from flask_restx import Api
from flask_restx import Namespace, Resource, fields
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import NotFound
from werkzeug.exceptions import InternalServerError

namespace = Namespace(name='Matrizes', description='Matrizes', path='/matrizes')

create_matriz = namespace.model('Dados para criação de Matrizes', {
    'rfid': fields.Integer(required=True, description='RFID'),
    'numero': fields.String(required=True, description='Número da matriz')
})

get_matriz = namespace.model('Consulta de matriz', {
    'id': fields.Integer(required=True, description='ID da matriz')
})

get_episode_response = namespace.model('Resposta pegar Matrizes', {
    'rfid': fields.Integer(required=True, description='Identificador único do matrizes'),
    'numero': fields.String(required=True, description='Nome do matrizes'),
    'url': fields.String(required=True, description='Url do matrizes')
})

list_episodes = namespace.model('Lista de matrizess', {
    'id': fields.Integer(required=True, description='Identificador único do Matrizes'),
    'name': fields.String(required=True, description='Nome do matrizes'),
    'url': fields.String(required=True, description='Url do matrizes')
})

list_episodes_response = namespace.model('Resposta da lista de matrizess', {
    'list': fields.Nested(list_episodes, required=True, description='Lista de matrizess')
})

delete_episode_response = namespace.model('Resposta da remocao de matrizes', {
    'removed': fields.Boolean(required=True, description='Indicador de remocao com sucesso')
})

headers = namespace.parser()
# Aqui podemos adicionar mais parametros ao headers

@namespace.route('/create')
@namespace.expect(headers)
@namespace.param('body')
class CreateEpisode(Resource):
    @namespace.expect(create_matriz, validate=True)
    def post(self):
        """Cadastra uma nova matriz"""
        try:
            return '{"teste": "teste"}'
            #return matrizCRUD.cadastrarMatriz(create_matriz)
        except Exception as e:
            raise InternalServerError(e.args[0])
        finally:
            raise InternalServerError(e.args[0])

@namespace.route('/<int:id>')
@namespace.param('id')
@namespace.expect(headers)
class GetMatriz(Resource):
    def get(self, id):
        """Consulta uma matriz por id"""
        try:
            matriz = matrizCRUD.consultarMatriz(id)
            return matriz
        except HTTPException as e:
            raise InternalServerError(e.args[0])


@namespace.route('/get', doc={"description": 'Lista todos os matrizess'})
@namespace.expect(headers)
class ListEpisodes(Resource):
    @namespace.response(200, 'Success')
    @namespace.response(404, 'Not Found Error')
    @namespace.response(500, 'Server Error')
    @namespace.marshal_with(list_episodes_response)
    def get(self):
        """Lista todos os matrizess"""
        session = db.session
        try:
            return ""
        except HTTPException as e:
            raise e
        except Exception as e:
            raise InternalServerError(e.args[0])
        finally:
            session.close()


@namespace.route('/remove/<int:id>',
                 doc={"description": 'Apaga matrizes'})
@namespace.param('id', 'ID da matriz')
@namespace.expect(headers)
class DeleteProducers(Resource):
    @namespace.response(200, 'Success')
    @namespace.response(500, 'Server Error')
    @namespace.marshal_with(delete_episode_response)
    def delete(self, producer_id, id):
        """Remove matrizes"""
        try:
            return ""
        except Exception as e:
            raise InternalServerError(e.args[0])
        finally:
            raise InternalServerError(e.args[0])

def bind_with_api(api: Api):
    """
    Adiciona o namespace à API recebida
    :param api: Flask Restplus API
    :return: Vazio
    """
    api.add_namespace(namespace)
    return None