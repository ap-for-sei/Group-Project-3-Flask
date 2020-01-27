import datetime
from peewee import *
from flask_login import UserMixin

DATABASE = PostgresqlDatabase('pro_app')

class User(UserMixin, Model):
    username = CharField(unique = True, null = False)
    email = CharField(unique = True, null = False)
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

class Message(Model):
    name = CharField()
    body = CharField()
    topic = ForeignKeyField(Board, backref = 'messages')
    auther = ForeignKeyField(User, backref = 'messages')
    created_at = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Board], safe = True)
    print("TABLES Created")
    DATABASE.close()