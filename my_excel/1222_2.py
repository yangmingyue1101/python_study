# -*-coding:UTF-8 -*-
from pymysql import connect

conn=connect(host='192.168.1.4', user='root', password="root",database='cms', port=3306)
cursor=conn.cursor()
cursor.execute('select * from yue_student')
result=cursor.fetchall()
print(result)





    

