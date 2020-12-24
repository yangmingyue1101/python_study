# -*-coding:UTF-8 -*-
from time import sleep

from pymysql import connect
from selenium import webdriver



driver=webdriver.Chrome(r'../drivers/chromedriver.exe')
driver.get('http://192.168.1.4/ecshop/admin/privilege.php?act=login')
driver.maximize_window()
driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()

driver.switch_to.frame('menu-frame')
driver.find_element_by_link_text('商品列表').click()
driver.switch_to.default_content()
driver.switch_to.frame('main-frame')

goods_name=driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span').text
print(driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span').text)
driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[12]/a[4]/img').click()

driver.switch_to.alert.accept()
sleep(3)
conn=connect('192.168.1.4','root','root','ecshop',3306)
cursor=conn.cursor()
cursor.execute("select is_delete from ecs_goods where goods_name='%s'" % goods_name)
result=cursor.fetchone()
print(result)
if result[0]==1:
    print('测试成功')
else:
    print('测试不成功')
