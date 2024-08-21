from peewee import Model, CharField, ForeignKeyField, AutoField, DoubleField

from config.database import database
from models.residencia import Residencia
from models.comodo import Comodo

class DispositivoEletrico(Model):
    id = AutoField()
    nome = CharField()
    consumo = DoubleField()
    uso_diario = DoubleField()
    comodo = ForeignKeyField(Comodo, backref='dispositivos')
    residencia = ForeignKeyField(Residencia, backref='dispositivos')

    class Meta:
        database = database
