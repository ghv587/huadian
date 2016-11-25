import tornado.web


class HostmanagerHandle(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('hostmanager.html')