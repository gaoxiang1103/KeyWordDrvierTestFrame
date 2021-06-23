from demo03 import mysql

insert = 'insert into My_Test(name,age) values(%s,%s)'
values1 = ([('dalang', '16'), ('erlang', '15')])
test1 = mysql().insert_sql(insert,values1)
print(test1)

delete = 'delete from my_test where name = "damao"'
test2 = mysql().delete_sql(delete)
print(test2)

update = 'update my_test set age = 11 where name = "dalang"'
test3 = mysql().update_sql(update)
print(test3)

select= 'select id,name,age from my_test order by age asc'
test4 = mysql().select_sql(select)
print(test4[0][2])