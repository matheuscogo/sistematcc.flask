from flask import render_template, request, Blueprint, redirect
import json

bp_controller = Blueprint('route', __name__)


@bp_controller.route('/api/cadastrarMatriz', methods=['POST', 'GET'])
def cadastrarMatriz():  # Cadastrar Matriz
    try:
        templateData = {
            'title': 'Sistema de gerenciamento de matrizes',
            'overview': 'Matrizes',
            'color': 'green',
        }
        return render_template("index.html", **templateData)
    except BaseException as e:
        templateData = {
            'title': 'Sistema de gerenciamento de matrizes',
            'color': 'green',
            'aviso': "Erro ao cadastrar Matriz"
        }
        return "isso é o cadastra matriz teste"
