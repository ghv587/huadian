#encoding=utf-8
import tornado
import tornado.web
import os


class PingHandle(tornado.web.RequestHandler):
    # def get(self, *args, **kwargs):
    #     os.system('python ping.py > ping.txt')
    #     output = os.popen('cat ping.txt')
    #     pingresult = output.read()
    #     self.render('ping.html',pingresult=pingresult)
    def get(self, *args, **kwargs):
        os.system('python ping.py > ping.txt')
        with open('ping.txt','r') as f:
            relist = f.readlines()
        self.render('ping.html',relist=relist)


