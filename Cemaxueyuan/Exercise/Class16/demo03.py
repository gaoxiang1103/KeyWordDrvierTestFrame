import pymysql
import configparser

class mysql():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('db.ini', encoding='utf-8')
        host = config['TestDB']['host']
        port = int(config['TestDB']['port'])
        user = config['TestDB']['user']
        password = config['TestDB']['password']
        database = config['TestDB']['database']
        try:
            self.con = pymysql.connect(host=host, port=port, user=user, password=password,database=database)
        except Exception as e:
            print('数据库连接异常，异常信息为%s'%(e))

        self.cur = self.con.cursor()

    def insert_sql(self, insert, values):
        self.cur.executemany(insert, values)
        self.cur.execute('commit')
        self.cur.close()
        return True

    def delete_sql(self, delete):
        self.cur.execute(delete)
        self.cur.execute('commit')
        self.cur.close()
        return True

    def update_sql(self,update):
        self.cur.execute(update)
        self.cur.execute('commit')
        self.cur.close()
        return True

    def select_sql(self, select):
        self.cur.execute(select)
        result = self.cur.fetchall()
        return result
