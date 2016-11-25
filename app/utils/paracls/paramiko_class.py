import paramiko
import ConfigParser


# class ParamikoClient:
#     def __init__(self):
#         self.conf = ConfigParser.ConfigParser()
#         self.conf.read("../../../config/config.ini")
#         self.client = paramiko.SSHClient()
#         self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     def connect(self):
#         try:
#             host = self.conf.get("section1", "host")
#             user = self.conf.get("section1", "user")
#             passwd = self.conf.get("section1", "passwd")
#             self.client.connect(hostname='host', username='user', password='passwd')
#         except Exception,e:
#             print e
#             try:
#                 self.client.close()
#             except:
#                 pass
#     def run_cmd(self,cmd_str):
#         stdin,stdout,stderr = self.client.exec_command(cmd_str)
#         for line in stdout:
#             print line
#
#
# client = ParamikoClient()
# client.connect()
# client.run_cmd('data')

# import paramiko
#
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect("127.0.0.1",22,"zzp","zzp")
# stdin,stdout,stderr = ssh.exec_command("cat /proc/meminfo")
# for i in stdout:
#     print i
# # print stdout.readlines()
# ssh.close()


def pexc_cmd(cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("127.0.0.1", 22, "zzp", "zzp")
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print stdout.readlines()[0]