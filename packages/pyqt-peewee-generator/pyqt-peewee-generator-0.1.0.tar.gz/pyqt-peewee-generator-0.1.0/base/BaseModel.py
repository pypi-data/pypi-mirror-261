from peewee import SqliteDatabase, Model, PrimaryKeyField

db = SqliteDatabase("database.db")


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
