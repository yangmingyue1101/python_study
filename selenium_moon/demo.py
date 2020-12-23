# -*-coding:UTF-8 -*-
from time import sleep

from pymysql import connect
from selenium import webdriver


driver=webdriver.Chrome('../drivers/chromedriver.exe')
driver.get('http://192.168.1.4/ecshop/admin/privilege.php?act=login')
driver.maximize_window()
driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()
driver.switch_to.frame('menu-frame')
driver.find_element_by_link_text('商品列表').click()
driver.switch_to.default_content()
driver.switch_to.frame('main-frame')
driver.find_element_by_name('keyword').send_keys('车')
driver.find_element_by_xpath("//input[@value=' 搜索 ']").click()
sleep(2)
web_result=driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span').text
web_pages=driver.find_element_by_id('totalRecords').text
conn=connect('192.168.1.4','root','root','ecshop',3306)
cursor=conn.cursor()
cursor.execute("select goods_name from ecs_goods where goods_name like'%车%'")
result=cursor.fetchall()
print(result[0][0])
cursor.execute("select count(*) from ecs_goods where goods_name like'%车%'")
total_page=cursor.fetchall()
print(total_page[0][0])


if web_result==result[0][0] and int(web_pages) == total_page[0][0]:
    print('测试通过')
else:
    print("测试不通过")
cursor.close()
conn.close()