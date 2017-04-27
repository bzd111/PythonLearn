# -*- coding: utf-8 -*-
from datetime import datetime

from config import DB_HOST
from config import DB_PORT
from mongoengine import connect
from mongoengine import DateTimeField
from mongoengine import Document
from mongoengine import ListField
from mongoengine import ReferenceField
from mongoengine import StringField

connect(db="fromoffice", host=DB_HOST, port=DB_PORT)


# һ�Զ��ϵ
class User(Document):
    name = StringField()
    # meta = {'collecion': 'user'}


class Page(Document):
    content = StringField()
    authors = ListField(ReferenceField(User))
    # meta = {'collection':'page'}

# User.drop_collection()
# Page.drop_collection()
#
# bob =User(name="Bob Jones").save()
# john = User(name="John Smith").save()
# for user in User.objects:
#     print(user.name)
#
# Page(content="Test Page",authors=[bob,john]).save()
# Page(content="Another Page",authors=[bob]).save()

#
# print(Page.objects(authors__in=[bob]))
# print(Page.objects(authors__in=[bob,john]))
# for page in Page.objects(authors__in=[bob]):
#     print("the page content",page.content)
#     for user in page.authors:
#         print("the page user",user.name)

# print(Page.objects(id=Page.objects(authors__in=[bob,john]).first.id).update_one(pull__authors=[bob]))
# print(Page.objects(id="....").update_one(push__authors=[bob,john]))


class Pages(Document):
    title = StringField(max_length=200, required=True, default="123123")
    meta = {"allow_inheritance": True}


class DatePage(Pages):

    data = DateTimeField()


d1 = DatePage(data=datetime.now())
d1.save()
print("ok")
