# -*-coding:UTF-8 -*-
from xlwt.Formatting import Borders, Font, Alignment, Pattern
from xlwt.Style import XFStyle
from xlwt.Workbook import Workbook


wb=Workbook('utf-8')
sheet=wb.add_sheet('测试报告')
sheet.write(1,1,'自动化测试点')



title=['编号', '姓名', '职业', '上级', '入职日期']
title_style=XFStyle()
border=Borders()
border.left=border.THIN
border.right=border.THIN
border.top=border.THIN
border.bottom=border.THIN

font=Font()
font.blod=True

alignment=Alignment()
alignment.horz=alignment.HORZ_CENTER

pattern=Pattern()
pattern.pattern=pattern.SOLID_PATTERN
pattern.pattern_fore_colour=0x35

title_style.borders=border
title_style.font=font
title_style.alignment=alignment
title_style.pattern=pattern

for i in range(len(title)):
    sheet.write(4,4+i,title[i],title_style)
    
content=[[7369,'SMITH','CLERK',7902,'12/17/1980'],
         [7499,'ALLEN','SALESMAN',7698,'2/20/1981'],[7521,'WARD','SALESMAN',7698,'2/22/1981'],[7566,'JONES','MANAGER',7839,'4/2/1981'],[7654,'MARTIN','SALESMAN',7698,'9/28/1981']]
content_style=XFStyle()
# border=Borders()
# border.left=border.THIN
# border.right=border.THIN
# border.top=border.THIN
# border.bottom=border.THIN

alignment=Alignment()
alignment.horz=alignment.HORZ_CENTER

# content_style.borders=border
content_style.alignment=alignment

for i in range(len(content)):
    for j in range(len(content[i])):
        sheet.write(i+5,j+4,content[i][j],content_style)
wb.save(r'd:\自动化测试.xls')

