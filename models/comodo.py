from peewee import Model, CharField, ForeignKeyField, AutoField

from config.database import database
from models.residencia import Residencia

class Comodo(Model):
    id = AutoField()
    nome = CharField()
    residencia = ForeignKeyField(Residencia, backref='comodos')

    class Meta:
        database = database