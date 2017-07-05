# coding:utf-8

import os

import tornado.web
import tornado.ioloop


INPUT_LIST = []


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        val = self.get_argument('val', None)
        if val:
            INPUT_LIST.append(val)
        self.render('template/index.html', input_list=INPUT_LIST)


settings = {
    "tempalte_path": "template",
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "static_url_perfix": "/img/",
}

application = tornado.web.Application([
    (r'/', MainHandler),
], **settings)


if __name__ == "__main__":
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
