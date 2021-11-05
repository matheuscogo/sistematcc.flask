from ...db import db, ma
from .Confinamento import association_table

class Matriz(db.Model):
    __tablename__ = "matrizes"
    __table_args__ = {'extend_existing': True}
    id = db.Column("id", db.Integer, primary_key=True)
    rfid = db.Column("rfid", db.VARCHAR)
    numero = db.Column("numero", db.Integer)
    ciclos = db.Column("ciclos", db.Integer)
    
    def __repr__(self):
        return '<Matriz {}>'.format(self.rfid)

class MatrizSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Matriz
        include_fk = False