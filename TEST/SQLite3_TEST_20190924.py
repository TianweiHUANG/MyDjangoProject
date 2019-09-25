import sqlite3

conn = sqlite3.connect('TEST.db')#连接
cursor = conn.cursor()#光标

#创建表格
#cursor.execute('create table TEST_Tal(id integer primary key autoincrement,name varchar(20) not null)')
#插入记录
#cursor.execute('insert into TEST_Tal (ID, NAME) values (1,"JACK")')
#更新记录
#cursor.execute('UPDATE TEST_Tal SET NAME= "MARY" WHERE ID = 1')
#删除记录
#cursor.execute('DELETE FROM TEST_Tal WHERE ID = 1')
#查询记录
cursor.execute('SELECT * FROM TEST_Tal')
for row in cursor:
    print("%s %s"%(row[0],row[1]))

cursor.close()#关闭光标
conn.commit()#提交
conn.close()#关闭连接