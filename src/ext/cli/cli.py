from ..site.model import Matriz
from ..site.model import Usuario
from ..site.model import Registro
from ..db import db


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()
