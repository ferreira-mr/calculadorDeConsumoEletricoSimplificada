from peewee import AutoField, CharField, DoubleField, ForeignKeyField, Model

from config.database import database
from models.comodo import Comodo
from models.residencia import Residencia


class DispositivoEletrico(Model):
    id = AutoField()
    nome = CharField()
    consumo = DoubleField()
    uso_diario = DoubleField()
    comodo = ForeignKeyField(Comodo, backref='dispositivos')
    residencia = ForeignKeyField(Residencia, backref='dispositivos')

    class Meta:
        database = database
