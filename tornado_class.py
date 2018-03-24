import tornado.ioloop
import tornado.web
import os


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
    PORT = int(os.environ.get('PORT', '8888'))
    app.listen(PORT)
    #event loop
    tornado.ioloop.IOLoop.current().start()
