# -*-coding:UTF-8 -*-
from xlrd import open_workbook
class Myexcel():
    def __init__(self, workbook_name, sheet_name):
        self.workbook_name = workbook_name
        self.sheet_name = sheet_name
        
    def sheet(self):
        bk=open_workbook(self.workbook_name)
        sheet=bk.sheet_by_name(self.sheet_name)
        return sheet
my=Myexcel(r'd:\doc\emp.xls','empinfo')
