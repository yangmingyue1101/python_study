# -*-coding:UTF-8 -*-

from pymysql import connect
from selenium import webdriver
from selenium.webdriver.support.select import Select
from xlrd import open_workbook


wb=open_workbook(r'd:\emp.xls')
sheet=wb.sheet_by_name('商品名称')
values=sheet.col_values(0,0)
for i in range(len(values)):    
    driver=webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get('http://192.168.1.4/ecshop/admin/privilege.php?act=login')
    driver.maximize_window()
    driver.find_element_by_name('username').send_keys('caichang')
    driver.find_element_by_name('password').send_keys('caichang1')
    driver.find_element_by_class_name('btn-a').click()
     
    driver.switch_to.frame('menu-frame')
    driver.find_element_by_link_text('添加新商品').click()
    driver.switch_to.default_content()
    driver.switch_to.frame('main-frame')
    driver.find_element_by_name('goods_name').send_keys('%s' %values[i])
    Select(driver.find_element_by_name('cat_id')).select_by_visible_text('    小型手机')
    driver.find_element_by_xpath("//input[@value=' 确定 ']").click()
     
    conn = connect('192.168.1.4','root','root','ecshop',3306)
    cursor = conn.cursor()
    cursor.execute("select goods_name from ecs_goods where goods_name='%s'" %values[i])
    result=cursor.fetchone()
    if result==values[i]:
        print('测试通过')
    else:
        print('测试不通过')
driver.close()
conn.close()
cursor.close()
    




    
    