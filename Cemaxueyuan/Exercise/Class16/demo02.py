import pymysql

class mysql():
    def __init__(self):
        try:
            self.con = pymysql.connect(host='127.0.0.1', port=3307, user='bitnami', password='7de4df210b',
                                       database='bitnami_redmine')
        except Exception as e:
            print(e)

        self.cur = self.con.cursor()

    def insert_sql(self, insert, values):
        self.cur.executemany(insert, values)
        self.cur.execute('commit')
        self.cur.close()
        return True

    def select_sql(self, select):
        self.cur.execute(select)
        result = self.cur.fetchall()
        return result
