# -*- coding: utf-8 -*-
import datetime

from config import DATABASE_NAME
from config import DB_HOST
from config import DB_PORT
from mongoengine import connect
from mongoengine import DateTimeField
from mongoengine import Document
from mongoengine import StringField


connect(DATABASE_NAME, host=DB_HOST, port=DB_PORT)


class BaseModel(Document):

    create_at = DateTimeField(default=datetime.datetime.now())
    print(create_at)

    meta = {'allow_inheritance': True,
            'abstract': True}


class DiskModle(BaseModel):

    disk_name = StringField(max_length=30)
    total_space = StringField(max_length=10)
    used_space = StringField(max_length=10)
    free_space = StringField(max_length=10)
    perent = StringField(max_length=10)

    meta = {'colletcion': 'disk'}


class MemModle(BaseModel):

    total = StringField(max_length=15)
    used = StringField(max_length=15)
    free = StringField(max_length=15)

    @classmethod
    def from_dict(cls, data_list):
        print("class init data", data_list)
        return cls(**data_list)

    meta = {'collecion': 'mem'}
