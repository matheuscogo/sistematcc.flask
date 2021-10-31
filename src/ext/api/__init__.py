from flask import Blueprint
from flask_restx import Api
from .routes import matrizes, planos, registros, confinamento, dias, usuarios

api = Api(
    Blueprint('API - Vult Scire', __name__),
    title='API para gestão do sistema de alimentação de matrizes de suinas',
    version='1.0',
    description='Endpoints para criação, consulta, alteração e exclusão para cosumo.'
)

# Atrela o namespace à API de podcast
matrizes.bind_with_api(api)
planos.bind_with_api(api)
registros.bind_with_api(api)
confinamento.bind_with_api(api)
dias.bind_with_api(api)
usuarios.bind_with_api(api)

def init_app(app):
    app.register_blueprint(api.blueprint, url_prefix='/api/v1.0')
