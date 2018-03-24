import tornado.ioloop
import tornado.web


#handles response when URL is visited
#is class and inherits from request handler
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, Katy")


class page2Handler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, Chris")


class page3Handler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, William")


def make_app():
    return tornado.web.Application(
        [
            #home page
            (r"/", MainHandler),
            (r"/page2", page2Handler),
            (r"/page3", page3Handler),
        ],
        autoreload=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
