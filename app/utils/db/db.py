#coding:utf-8

from config.define import *
import torndb
import MySQLdb

db = torndb.Connection(user=options.mysql_user,
                       password=options.mysql_password,
                       host=options.mysql_host,
                       database=options.mysql_database, )


class db_operation(object):
    def __init__(self,sql):
        try:
            db = torndb.Connection(user=options.mysql_user,
                                   password=options.mysql_password,
                                   host=options.mysql_host,
                                   database=options.mysql_database, )
            self.sql = sql
            self.db = db
        except Exception,e:
            print '数据库连接失败!'

    def select(self):
        try:
            select_data = self.db.query(self.sql)
            return select_data
        except Exception,e:
            print self.sql
            print 'SQL 语法有问题!'
        finally:
            self.db.close()

    def update(self):
        try:
            update_data = self.db.execute(self.sql)
            return update_data
        except Exception,e:
            print self.sql
            print 'SQL 语法有问题!'
        finally:
            self.db.close()

    def delete(self):
        try:
            delete_data = self.db.execute(self.sql)
            return delete_data
        except Exception,e:
            print self.sql
            print 'SQL 语法有问题!'
        finally:
            self.db.close()



