'''
@auther:高翔
@email:gaoxiang1103@163.com
@time:2021/5/29
'''
import pymysql

con = pymysql.connect(host='127.0.0.1',port=3307,user='bitnami',password='7de4df210b',database='bitnami_redmine')

# 创建游标
cur = con.cursor()
# 创建表
# sql ='CREATE TABLE My_Test(ID INT PRIMARY KEY auto_increment, NAME VARCHAR(200), AGE INT)'
# cur.execute(sql)
# con.close()

# 增删改
# sql = 'insert into My_Test(name,age) values("xiaoming","32")'
# cur.execute(sql)
# cur.execute('commit')
# con.close()

# 插入多条数据
sql = 'insert into My_Test(name,age) values(%s,%s)'
value = ([('xiaoli','33'),('xiaojian','35')])
cur.executemany(sql,value)
cur.execute('commit')
con.close()

# 查询数据
# sql = 'select * from my_test'
# cur.execute(sql)
# result = cur.fetchmany(2)
# print(result)
