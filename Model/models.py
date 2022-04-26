from mongoengine import *
from datetime import datetime
from numpy import unique
from App import db

class User(Document):
    fullname = StringField(max_length=64, required=True, unique=True)

class Session(EmbeddedDocument):
    active = DateTimeField(default=datetime.now())
    expire = IntField(default=300)
    sid = StringField(max_length=16, unique=True)

class Account(EmbeddedDocument):
    email = EmailField(required=True, unique=True)
    password = StringField(min_length=6)