# -*-coding:UTF-8 -*-
from xlrd import open_workbook
bk=open_workbook(r'd:\doc\emp.xls')
sheet=bk.sheet_by_name('empinfo')
print(sheet.nrows)

bk=open_workbook(r'd:\doc\emp.xls')
sheet=bk.sheet_by_name('empinfo')
print(sheet.ncols)

bk=open_workbook(r'd:\doc\emp.xls')
sheet=bk.sheet_by_name('empinfo')
cell_value=sheet.cell_value(12,6)
print(cell_value)

bk=open_workbook(r'd:\doc\emp.xls')
sheet=bk.sheet_by_name('empinfo')
col_values=sheet.col_values(6,4)
print(col_values)

bk=open_workbook(r'd:\doc\emp.xls')
sheet=bk.sheet_by_name('empinfo')
col_values = sheet.col_values(5,5)
print(col_values)

bk=open_workbook(r'd:\doc\emp.xls')
sheet=bk.sheet_by_name('empinfo')
row_values = sheet.row_values(5,4)
print(row_values)

lists=[]
for i in range(5,13):
   ii=sheet.row_values(i,4)
   lists.append(ii)
   print(lists)
   






