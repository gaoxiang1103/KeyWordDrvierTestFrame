from demo02 import mysql

sql1 = 'insert into My_Test(name,age) values(%s,%s)'
values1 = ([('damao', '16'), ('ermao', '15')])

test1 = mysql().insert_sql(sql1,values1)
print(test1)

sql2= 'select id,name,age from my_test'
test2 = mysql().select_sql(sql2)
print(test2)