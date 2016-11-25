import os
import ConfigParser





def hostsnmp():
    host_result=os.system('snmpwalk -v 2c -c checr 10.102.1.10 1.3.6.1.2.1.2')


