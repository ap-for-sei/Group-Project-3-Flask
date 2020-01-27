import datetime
from peewee import *
from flask_login import UserMixin

DATABASE = PostgresqlDatabase('board_app')

class User(UserMixin, Model):
    username = CharField(unique = True)
    email = CharField(unique = True)
    password = CharField()

    class Meta: 
        database = DATABASE

class Board(Model):
    name = CharField()
    body = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    loggedUser = ForeignKeyField(User, backref = 'boards')

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Board], safe = True)
    print("TABLES Created")
    DATABASE.close()