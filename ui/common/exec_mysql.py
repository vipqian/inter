import pymysql
from ui.common.log import logger
import threading
import configparser

mutex=threading.Lock()
mutex.acquire() # 上锁，防止多线程下出问题
conf = configparser.ConfigParser()
conf.read(r"F:/automation/ui/config/mysql.ini", encoding='utf-8')
if conf.get('select', 'select') == '1':
    host = conf.get('testmysql', 'host')
    port = int(conf.get('testmysql', 'port'))
    user = conf.get('testmysql', 'user')
    passwd = conf.get('testmysql', 'passwd')
    db = conf.get('testmysql', 'db')
else:
    host = conf.get('mysql', 'host')
    port = int(conf.get('mysql', 'port'))
    user = conf.get('mysql', 'user')
    passwd = conf.get('mysql', 'passwd')
    db = conf.get('mysql', 'db')
# print(host, port, user, passwd, db)
mutex.release()


class ExecMysql():
    log = logger

    def select_mysql(self, sql):
        try:
            connect = pymysql.connect(
                host=host,
                port=port,
                user=user,
                passwd=passwd,
                db=db,
            )
            cursor = connect.cursor()
            cursor.execute(sql)
            row = cursor.fetchall()
            return row
        except Exception as msg:
            self.log.info(str(msg))
        finally:
            cursor.close()
            connect.close()

    def insert_mysql(self, sql):
        try:
            connect = pymysql.connect(
                host=host,
                port=port,
                user=user,
                passwd=passwd,
                db=db,
            )
            cursor = connect.cursor()
            cursor.execute(sql)
            connect.commit()
        except Exception as msg:
            self.log.info(str(msg))
        finally:
            cursor.close()
            connect.close()

    def delete_mysql(self, sql):
        try:
            connect = pymysql.connect(
                host=host,
                port=port,
                user=user,
                passwd=passwd,
                db=db,
            )
            cursor = connect.cursor()
            cursor.execute(sql)
            connect.commit()
        except Exception as msg:
            self.log.info(str(msg))
        finally:
            cursor.close()
            connect.close()

    def update_mysql(self, sql):
        try:
            connect = pymysql.connect(
                host=host,
                port=port,
                user=user,
                passwd=passwd,
                db=db,
            )
            cursor = connect.cursor()
            cursor.execute(sql)
            connect.commit()
        except Exception as msg:
            self.log.info(str(msg))
        finally:
            cursor.close()
            connect.close()


if __name__ == '__main__':
    a = ExecMysql()
    sql = "SELECT * FROM trade;"
    sql1 = "INSERT INTO trade(user, account) VALUE ('zhang', '1445123');"
    sql2 = "SHOW TABLES;"
    a.insert_mysql(sql1)
    b = a.select_mysql(sql2)
    for i in b:
        print(i)



