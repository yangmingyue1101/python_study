# -*-coding:UTF-8 -*-
from pymysql import connect
from xlwt.Workbook import Workbook
conn = connect(host='192.168.1.4', user='root', password="root", database='cms', port=3306)
cursor = conn.cursor()

cursor.execute('select * from _cai_student_cai')
result = cursor.fetchall()

print(result)

wb=Workbook('utf-8')
sheet=wb.add_sheet('学生信息')
title=['编号', '姓名', '生日', '性别']
for i in range(len(title)):
    sheet.write(4,4+i,title[i])
for i in range(len(result)):
    for j in range(len(result[i])):
        sheet.write(i+5,j+4,result[i][j])
wb.save(r'd:\学生表.xls')