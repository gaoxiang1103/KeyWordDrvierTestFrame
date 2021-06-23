import pymysql
from demo02 import mysql

def insert_sql(insert,values):
    con = pymysql.connect(host='127.0.0.1', port=3307, user='bitnami', password='7de4df210b',database='bitnami_redmine')
    cur = con.cursor()
    cur.executemany(insert,values)
    cur.execute('commit')
    cur.close()
    return True

def select_sql(select):
    con = pymysql.connect(host='127.0.0.1', port=3307, user='bitnami', password='7de4df210b',database='bitnami_redmine')
    cur = con.cursor()
    cur.execute(select)
    result = cur.fetchall()
    return result




