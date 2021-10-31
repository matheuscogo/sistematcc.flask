from flask import Flask
from ext import db
from ext import config
from ext import api

def create_app():
    app = Flask(__name__)

    config.init_app(app)
    db.init_app(app)
    api.init_app(app)
    
    return app