# coding:utf-8
import hashlib
import json
import os
import uuid

import memcache
import tornado.ioloop
import tornado.web
# import simplejson as json


conn = memcache.Client(["10.1.10.51:11211"])


class MemcachedSession():
    CookieID = "name"
    ExpireTime = 60 * 10

    def __init__(self, handler):
        self.handler = handler
        SessionID = self.handler.get_secure_cookie(MemcachedSession.CookieID,
                                                   None)
        if SessionID and conn.get(SessionID):
            self.SessionID = SessionID
        else:
            self.SessionID = self.SessionKey()
            conn.set(self.SessionID, json.dumps({}),
                     MemcachedSession.ExpireTime)
        conn.set(self.SessionID, conn.get(self.SessionID),
                 MemcachedSession.ExpireTime)
        self.handler.set_secure_cookie(MemcachedSession.CookieID,
                                       self.SessionID)

    def SessionKey(self):
        UUID = str(uuid.uuid1()).replace("-", "")
        MD5 = hashlib.md5()
        MD5.update(bytes(str(UUID), encoding='utf-8'))
        # .update(bytes(str(time.time()), encoding='utf-8'))
        sessionkey = MD5.hexdigest()
        return sessionkey

    def __setitem__(self, key, value):
        SessionDict = json.loads(conn.get(self.SessionID))
        SessionDict.setdefault(key, value)
        conn.set(self.SessionID, json.dumps(SessionDict),
                 MemcachedSession.ExpireTime)

    def __getitem__(self, key):
        SessionDict = json.loads(conn.get(self.SessionID))
        ResultData = SessionDict.get(key, None)
        return ResultData

    def __delitem__(self, key):
        SessionDict = json.loads(conn.get(self.SessionID))
        del SessionDict[key]
        conn.set(self.SessionID, json.dumps(SessionDict),
                 MemcachedSession.ExpireTime)

    def GetAll(self):
        SessionData = conn.get(self.SessionID)
        # print(SessionData)
        SessionDict = json.loads(SessionData)
        return SessionDict


class BaseHandle(tornado.web.RequestHandler):
    def initialize(self):
        self.session = MemcachedSession(self)


class MainHandle(BaseHandle):
    def get(self, *args, **kwargs):
        # self.write("hello")
        Info = self.session.GetAll()
        self.render("template/index_memcache.html", Data=Info)

    def post(self, *args, **kwargs):
        # self.write("world")
        key = self.get_argument('key')
        value = self.get_argument('value')
        action = self.get_argument("action")
        print(self.session.SessionID)
        if action == "set":
            self.session[key] = value
        elif action == "del":
            del self.session[key]

        Info = self.session.GetAll()
        self.render("template/index_memcache.html", Data=Info)


settings = {
    "tempalte_path": os.path.join(os.path.dirname(__file__), "template"),
    "cookie_secret": "508CE6152CB93994628D3E99934B83CC",
}

application = tornado.web.Application([
    (r'/', MainHandle),
], **settings)

if __name__ == "__main__":
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
