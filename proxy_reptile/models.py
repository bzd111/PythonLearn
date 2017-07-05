# -*- coding: utf-8 -*-
import datetime

from mongoengine import (connect, StringField, DateTimeField, Document)
from config import DB_HOST, DB_PORT, DATABASE_NAME
connect(DATABASE_NAME, host=DB_HOST, port=DB_PORT)


class BaseModel(Document):
    create_at = DateTimeField(default=datetime.datetime.now)

    meta = {'allow_inheritance': True,
            'abstract': True}


class Proxy(BaseModel):

    address = StringField(unique=True)

    meta = {'colletcion': 'proxy'}
