import tornado.web
import paramiko
from app.utils.db.db import *
from app.utils.paracls.paramiko_class import *





class Exc_cmdHandle(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('application_manager.html')

    def post(self, *args, **kwargs):
        cmd = self.get_arguments("command")
        result = cmd
        # result = pexc_cmd(cmd)
        # ssh = paramiko.SSHClient()
        # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # ssh.connect("127.0.0.1", 22, "zzp", "zzp")
        # stdin, stdout, stderr = ssh.exec_command("cat /proc/meminfo")
        # # for i in stdout:
        # #     return i
        # # result=i[0]
        # result=stdout.readlines()[0]

        # ssh.close()
        self.render('application_manager2.html',result=result)
