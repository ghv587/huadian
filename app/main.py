#encoding:utf-8

import tornado.ioloop
import tornado.web
import tornado.auth
import tornado.httpserver
import os
from tornado.options import define,options
import torndb
from config.define import *
import MySQLdb
from app.utils.db.db import *
import logging
from app.handler.addhost import *
from app.handler.hostcheck import *
from peewee import *
from utils.peeweecls.monitorhost_model import *
from app.handler.hostmanager import *
from app.handler.netmanager import *




class BaseHandle(tornado.web.RequestHandler):

    def get_current_user(self):
        return self.get_secure_cookie("username")


class LoginHandle(BaseHandle):
    def get(self):
        self.render('login.html')

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        sql = 'select id from user where username=%s and password=%s'
        if db.get(sql, username, password) is None:
            return self.write(
                '''
                <script>
                    alert ("用户名或密码错误!")
                    window.location.href="/"
                </script>
                            ''')
        else:
            self.set_secure_cookie("username", self.get_argument("username"))  #"username"
            self.redirect('index')


class IndexHandle(BaseHandle):
    @tornado.web.authenticated
    def get(self, *args ,**kwargs):
        output1 = os.popen('free -m')
        time1=output1.read()
        output3 = os.popen('cat /proc/loadavg')
        cpu = output3.read()
        output4 = os.popen('date')
        time4 = output4.read()
        output2 = os.popen('df -lh')
        time2=output2.read()
        self.render('index.html',meminfo=time1,disk=time2,cpuinfo=cpu,time=time4)


class LogoutHandle(BaseHandle):
    def get(self):
        self.clear_cookie("username")
        self.redirect("/")



class Monitor_hostHandle(BaseHandle):
    @tornado.web.authenticated
    def get(self):
        host = Host.select().where(Host.ip == '192.168.1.1').get()
        self.render('monitor_host.html',host=host)

class Oper_fileHandle(BaseHandle):
    @tornado.web.authenticated
    def get(self):
        self.render('oper_file.html')

class Application_managerHandle(BaseHandle):
    @tornado.web.authenticated
    def get(self):
        self.render('application_manager.html')




class Monitor_performanceHandle(BaseHandle):
    @tornado.web.authenticated
    def get(self):
        # host = Host.select().where(Host.ip == '127.0.0.1').get()
        # ip = host.ip
        # os.environ['ip'] = str(ip)
        outputper = os.popen('snmpwalk -v 2c -c checr 10.102.248.41 1.3.6.1.2.1.25.2.2.0 ')
        perfor = outputper.read()
        self.render('monitor_performance.html',perfor=perfor)

class Monitor_deviceHandle(BaseHandle):
    @tornado.web.authenticated
    def get(self):
        outputdev = os.popen('snmpwalk -v 2c -c checr 10.102.1.41 1.3.6.1.2.1.2.2.1.2')
        device = outputdev.read()
        self.render('monitor_device.html',device=device)


class Monitor_logHandle(BaseHandle):
    @tornado.web.authenticated
    def get(self):
        self.render('monitor_log.html')

#______________________________________#


class WebApplication(tornado.web.Application):
    def __init__(self):
        handler = [
            (r"/index", IndexHandle),
            (r"/login", LoginHandle),
            (r"/", IndexHandle),
            (r"/logout", LogoutHandle),
            (r"/monitor_host", Monitor_hostHandle ),
            (r"/monitor_device", Monitor_deviceHandle),
            (r"/oper_file", Oper_fileHandle),
            (r"/application_manager", Application_managerHandle),
            (r"/monitor_log", Monitor_logHandle),
            (r"/monitor_performance", Monitor_performanceHandle),
 #------------------------------------------------------#operatehandler
            (r"/addhost", AddhostHandle),
            (r"/ping", PingHandle),
            (r"/hostmanager", HostmanagerHandle),
            (r"/netmanager", NetmanagerHandle),
                   ]

        settings = {
            'template_path':os.path.join(os.path.dirname(__file__),'../template'),
            'static_path':os.path.join(os.path.dirname(__file__),'../static'),
            'utils_path':os.path.join(os.path.dirname(__file__),'utils'),
            'config_path': os.path.join(os.path.dirname(__file__), '../config'),
            'debug': True,
            'login_url': '/login',
            'cookie_secret': '61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo='
        }

        super(WebApplication, self).__init__(handler , **settings)


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(WebApplication())
    http_server.listen(8899)

    options.parse_command_line()
    logging.debug("debug ...")
    tornado.ioloop.IOLoop.instance().start()


