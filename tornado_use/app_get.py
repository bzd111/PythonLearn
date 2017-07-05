# coding:utf-8

import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hello, World")


application = tornado.web.Application([
    (r'/', MainHandler),
])

if __name__ == "__main__":
    application.listen(8889)
    tornado.ioloop.IOLoop.instance().start()
