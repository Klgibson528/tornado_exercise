import tornado.ioloop
import tornado.web
import tornado.log
import os
import boto3

client = boto3.client(
    'ses',
    region_name='us-east-1',
    aws_access_key_id=os.environ.get('AWS_KEY'),
    aws_secret_access_key=os.environ.get('AWS_SECRET'))

from jinja2 import \
  Environment, PackageLoader, select_autoescape
ENV = Environment(
    loader=PackageLoader('jinja-app', 'templates'),
    autoescape=select_autoescape(['html', 'xml']))


def send_email(title, message):
    response = client.send_email(
        Destination={
            'ToAddresses': ['klgibson528@gmail.com'],
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': message,
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': title
            },
        },
        Source='klgibson528@gmail.com',
    )


class TemplateHandler(tornado.web.RequestHandler):
    def render_template(self, tpl, context):
        template = ENV.get_template(tpl)
        self.write(template.render(**context))


class MainHandler(TemplateHandler):
    def get(self):
        self.set_header('Cache-Control',
                        'no-store, no-cache, must-revalidate, max-age=0')

        context = {}

        self.render_template("hello.html", context)


class Page2Handler(TemplateHandler):
    def get(self):
        self.set_header('Cache-Control',
                        'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("page2.html", {})

    def post(self):
        email = self.get_body_argument('email')
        comment = self.get_body_argument('comments')
        message = email + '\n' + comment
        send_email('New Contact', message)
        self.set_header('Cache-Control',
                        'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("page2.html", {})


def make_app():
    return tornado.web.Application(
        [
            #home page
            (r"/", MainHandler),
            (r"/page2", Page2Handler),
            (r"/static/(.*)", tornado.web.StaticFileHandler, {
                'path': 'static'
            }),
        ],
        autoreload=True)


if __name__ == "__main__":
    tornado.log.enable_pretty_logging()
    app = make_app()
    PORT = int(os.environ.get('PORT', '8888'))
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()
