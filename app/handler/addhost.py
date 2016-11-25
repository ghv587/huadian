#encoding:utf-8
import paramiko
import tornado
import tornado.web
import paramiko
from app.main import BaseHandle
from peewee import *
from app.utils.peeweecls.monitorhost_model import *


class AddhostHandle(BaseHandle):
    def get(self, *args, **kwargs):
        self.render('addhost.html')


    def post(self, *args, **kwargs):
        ip = self.get_argument("ip")
        ostype  = self.get_argument("ostype")
        desc  = self.get_argument("desc")
        snmp = self.get_argument("snmp")
        db_ip = Host.create(ip=ip,ostype=ostype,desc=desc,snmp=snmp)
        self.write(                '''
                <script>
                    alert ("insert success")
                    window.location.href="addhost"
                </script>
                            ''')


