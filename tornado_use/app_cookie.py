# coding: utf-8
import os
import time

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        has_cookie = self.get_cookie("key", None)
        if not has_cookie:
            self.set_cookie("key", "val", expires=time.time() + 30)
            word = "Hello, World"
        else:
            word = has_cookie
        self.write(word)


class SecureHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        has_secure = self.get_secure_cookie("key", None)
        if not has_secure:
            self.set_secure_cookie("key", "value")
            word = "Hello, Secure"
        else:
            word = has_secure
        self.write(word)


class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.set_secure_cookie('username', 'zidy')
        self.set_secure_cookie('password', 'broada123')
        self.render('template/login.html')

    def post(self, *args, **kwargs):
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)
        cookie_user = str(self.get_secure_cookie('username'), encoding='utf-8')
        cookie_pass = str(self.get_secure_cookie('password'), encoding='utf-8')
        if username == cookie_user and password == cookie_pass:
            self.write("Hello, " + username)
        else:
            self.write("用户名或者密码错误")


settings = {
    "tempalte_path": os.path.join(os.path.dirname(__file__), "template"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "static_url_perfix": "/img/",
}

application = tornado.web.Application([
    (r'/', MainHandler),
    (r'/secure', SecureHandler),
    (r'/login', LoginHandler),
], cookie_secret="508CE6152CB93994628D3E99934B83CC", **settings)

if __name__ == "__main__":
    print("http://localhost:9999")
    print(settings['tempalte_path'])
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
