import tornado.web


class NetmanagerHandle(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('netmanager.html')