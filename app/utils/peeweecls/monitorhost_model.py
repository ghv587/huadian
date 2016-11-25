from peewee import *
import MySQLdb
from datetime import date

mysql_db = MySQLDatabase(host = '127.0.0.1', user = 'root', passwd = 'mysql', database = 'auto')

class Basedatabase(Model):
    class Meta:
        database = mysql_db

class Person(Basedatabase):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        db_tables = 'person'

class Host(Basedatabase):
    ip = CharField()
    desc = CharField()
    ostype = CharField()
    snmp = CharField()

    class Meta:
        db_tables = 'host'



# # mysql_db.create_table(Person)
# # mysql_db.connect()
#
# mysql_db.create_table(Host)



# uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
# uncle_bob.save()
# grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
# mes= []
# for host in Host.select():
#     mes.append(host)
#
# mes[0]

# host = Host.select().where(Host.ip == '127.0.0.1').get()
# Host.select().where(Host.id == 1).get()
