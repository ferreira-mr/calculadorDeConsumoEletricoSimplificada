from peewee import Model, CharField, AutoField


from config.database import database

class Residencia(Model):
    id = AutoField()
    proprietario = CharField()

    class Meta:
        database = database
