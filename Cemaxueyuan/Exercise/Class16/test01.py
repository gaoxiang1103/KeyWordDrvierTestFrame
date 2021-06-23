import demo01

sql1 = 'insert into My_Test(name,age) values(%s,%s)'
values1 = ([('dagou', '16'), ('ergou', '15')])

test1 = demo01.insert_sql(sql1,values1)
print(test1)

sql2= 'select id,name,age from my_test'
test2 = demo01.select_sql(sql2)
print(test2)
