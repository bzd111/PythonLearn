# coding: utf-8
import hashlib
import os
import uuid

import redis
import tornado.ioloop
import tornado.web


pool = redis.ConnectionPool(host="10.1.10.51", port=6379)
conn = redis.Redis(connection_pool=pool)


class RedisSeesion:
    CookieID = "name"
    ExpiresTime = 60 * 10

    def __init__(self, handler):
        self.handler = handler
        SessionID = self.handler.get_secure_cookie(RedisSeesion.CookieID, None)
        if SessionID and conn.exists(SessionID):
            self.SessionID = SessionID
        else:
            self.SessionID = self.SessionKey()
            conn.hset(self.SessionID, None, None)
        conn.expire(self.SessionID, RedisSeesion.ExpiresTime)
        self.handler.set_secure_cookie(RedisSeesion.CookieID, self.SessionID)

    def SessionKey(self):
        UUID = str(uuid.uuid1()).replace("-", "")
        MD5 = hashlib.md5()
        MD5.update(bytes(UUID, encoding="utf-8"))
        SessionKey = MD5.hexdigest()
        return SessionKey

    def __setitem__(self, key, value):
        conn.hset(self.SessionID, key, value)

    def __getitem__(self, key):
        return conn.hget(self.SessionID, key)

    def __delitem__(self, key):
        conn.hdel(self.SessionID, key)

    def GetAll(self):
        return conn.hgetall(self.SessionID)


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.session = RedisSeesion(self)


class MainHandler(BaseHandler):
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
    (r'/', MainHandler),
], **settings)

if __name__ == "__main__":
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
