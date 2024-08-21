from peewee import SqliteDatabase

DATABASE_PATH = 'database.db'

database = SqliteDatabase(DATABASE_PATH)


def startup_db():
    from models.comodo import Comodo
    from models.dispositivo import DispositivoEletrico
    from models.residencia import Residencia

    database.connect()
    database.create_tables([Residencia, Comodo, DispositivoEletrico])


def shutdown_db():
    database.close()
