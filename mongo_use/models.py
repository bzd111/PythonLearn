from mongoengine import connect,StringField,DateTimeField,Document
import datetime

from config import DB_HOST,DB_PORT,DATABASE_NAME


connect(DATABASE_NAME,host=DB_HOST,port=DB_PORT)

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

    # def __init__(self,name,total,used,free,perent):
    #
    #     self.disk_name = name
    #     self.total_space = total
    #     self.used_space = used
    #     self.free_space = free
    #     self.perent = perent
    #
    # @classmethod
    # def from_list(cls, data_list):
    #     return cls(*data_list)

    meta = {'colletcion': 'disk'}

class MemModle(BaseModel):

    total= StringField(max_length=15)
    used= StringField(max_length=15)
    free = StringField(max_length=15)

    # def __init__(self,total,used,free):
    #
    #     self.total = total
    #     self.used = used
    #     self.free = free

    @classmethod
    def from_dict(cls,data_list):
        print("class init data",data_list)
        return cls(**data_list)

    meta = {'collecion':'mem'}
