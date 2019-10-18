#for...in...TEST
for i in 'exampe199':#字符串
    print(type(i),i)
for i in ['Monday','Tuesday','Wednesday','Thursday','Friday']:#列表
    print(type(i), i)
for i in ('Tom','Jack','Cherry'):#元组
    print(type(i), i)
for i in {1000,3000,5000,7000,9000,10}:#集合
    print(type(i),i)
my_dict={"day1":"study","day2":"paly","day3":"sleep",'one':10,'two':20,'three':30,}#字典
print("---------- --- my_dict --- ----------")
for i in my_dict:
    print(type(i), i)
print("---------- my_dict.keys() ----------- ")
for i in my_dict.keys():
    print(type(i),i)
print("---------- my_dict.values() ----------")
for i in my_dict.values():
    print(type(i),i)
print("---------- my_dict.items() -----------")
for i,j in my_dict.items():
    print(type(i),type(j),i,j)

"""
#导入sqlite3
import sqlite3
#连接数据库
#如果数据库已存在，直接连接数据库；如果数据库不存在，先创建数据库，然后连接数据库
conn=sqlite3.connect('TEST.db')
#创建游标
cursor=conn.cursor()
#创建表
#cursor.execute('create table TEST_Tal(ID INT PRIMARY KEY, NAME VARCHAR(20) NOT NULL)')
#cursor.execute('create table TEST_Tal(id integer primary key autoincrement,name varchar(20) not null)')

#插入数据
#cursor.execute('insert into TEST_Tal (ID, NAME) values (1,"JACK")')
#更新数据
#cursor.execute('UPDATE TEST_Tal SET NAME= "TOM" WHERE ID = 1')
#删除数据
#cursor.execute('DELETE FROM TEST_Tal WHERE ID = 1')

#查询数据
cursor.execute('SELECT * FROM TEST_Tal')
TEST_Tal_list=cursor.fetchall()
print(type(TEST_Tal_list),TEST_Tal_list)

#关闭游标
cursor.close()
#提交事务
conn.commit()
#关闭连接
conn.close()
"""