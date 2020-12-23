# -*-coding:UTF-8 -*-
from xlrd import open_workbook
from xlutils.copy import copy
from xlwt.Formatting import Borders
from xlwt.Style import XFStyle


yuanshi_excel=open_workbook(r'd:\自动化测试.xls',formatting_info=True)
new_excel=copy(yuanshi_excel)
sheet=new_excel.get_sheet(0)
new_content=XFStyle()
border=Borders()
border.left=border.THIN
border.right=border.THIN
border.top=border.THIN
border.bottom=border.THIN

new_content.borders=border

sheet.write(3,5,5,new_content)
sheet.write(3,8,'mingyue',new_content)
new_excel.save(r'd:\新表副本.xls')


