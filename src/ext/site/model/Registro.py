from ...db import db, ma

class Registro(db.Model):
    __tablename__ = "registros"
    id = db.Column("id", db.Integer, primary_key=True)
    matriz = db.Column(db.Integer, db.ForeignKey("confinamento.matriz"))
    dataEntrada = db.Column("dataEntrada", db.VARCHAR)
    dataSaida = db.Column("dataSaida", db.VARCHAR)
    horaEntrada = db.Column("horaEntrada", db.VARCHAR)
    horaSaida = db.Column("horaSaida", db.VARCHAR)
    tempo = db.Column("tempo", db.VARCHAR)
    quantidade = db.Column("quantidade", db.Integer)

    def __init__(
        id = id,
        matriz = matriz,
        dataEntrada = dataEntrada,
        dataSaida = dataSaida,
        horaEntrada = horaEntrada,
        horaSaida = horaSaida,
        tempo = tempo,
        quantidade = quantidade
    ):
        Registro.id = id
        Registro.matriz = matriz
        Registro.dataEntrada = dataEntrada
        Registro.dataSaida = dataSaida
        Registro.dataSaida = dataSaida
        Registro.horaEntrada = horaEntrada
        Registro.horaSaida = horaSaida
        Registro.tempo = tempo
        Registro.quantidade = quantidade

class RegistroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Registro
        include_fk = False