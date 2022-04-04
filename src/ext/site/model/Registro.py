from ...db import db, ma

class Registro(db.Model):
    __tablename__ = "registros"
    id = db.Column("id", db.Integer, primary_key=True)
    matrizId = db.Column(db.Integer, db.ForeignKey("confinamento.matrizId"))
    dataEntrada = db.Column("dataEntrada", db.VARCHAR)
    dataSaida = db.Column("dataSaida", db.VARCHAR)
    horaEntrada = db.Column("horaEntrada", db.VARCHAR)
    horaSaida = db.Column("horaSaida", db.VARCHAR)
    tempo = db.Column("tempo", db.VARCHAR)
    quantidade = db.Column("quantidade", db.Integer)

class RegistroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Registro
        include_fk = True