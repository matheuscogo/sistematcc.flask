from flask import render_template, request, Blueprint, redirect
from datetime import datetime

bp_controller = Blueprint('route', __name__)


@bp_controller.route('/api/cadastrarMatriz', methods=['POST', 'GET'])
def cadastrarMatriz():  # Cadastrar Matriz
    try:  
        return {'time': datetime.now().strftime("%H:%M:%S")}
    except BaseException as e:
        return {'time': datetime.now().strftime("%H:%M:%S")}
