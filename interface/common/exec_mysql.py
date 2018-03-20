import pymysql
from ui.common.log import logger
import threading
import configparser

mutex=threading.Lock()
mutex.acquire() # 上锁，防止多线程下出问题
conf = configparser.ConfigParser()
conf.read(r"F:/automation/interface/config/mysql.ini", encoding='utf-8')
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


def fun_select():
    a = ExecMysql()
    sql = "SELECT * FROM trade;"
    b = a.select_mysql(sql)
    for i in b:
        print(i)

if __name__ == '__main__':
    mysql = ExecMysql()
    #查询
    select_sql = "SELECT * FROM trade;"
    result = mysql.select_mysql(select_sql) #得到的为元组
    for i in result:
        print(i)
    print('-' * 100)
    # 插入数据
    insert_sql = "INSERT INTO trade(user, account) VALUE ('cai23', '1234');"
    mysql.insert_mysql(insert_sql)
    fun_select()
    print('-'*100)
    # 更新数据
    update_sql = "UPDATE trade SET user='fei' WHERE id=32;"
    mysql.update_mysql(update_sql)
    fun_select()
    print('-' * 100)
    #删除数据
    delete_sql = "DELETE FROM trade WHERE id=32;"
    mysql.delete_mysql(delete_sql)
    fun_select()

