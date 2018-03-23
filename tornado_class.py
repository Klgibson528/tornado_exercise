import tornado.ioloop
import tornado.web


#handles response when URL is visited
#is class and inherits from request handler
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, Katy")


def make_app():
    return tornado.web.Application([
        #home page
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    #event loop
    tornado.ioloop.IOLoop.current().start()
