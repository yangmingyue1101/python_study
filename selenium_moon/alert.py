# -*-coding:UTF-8 -*-
from selenium import webdriver
driver=webdriver.Chrome(r'../drivers/chromedriver.exe')
driver.get('http://192.168.1.4/ecshop/admin/privilege.php?act=login')
driver.maximize_window()
driver.find_element_by_class_name('btn-a').click()
driver.switch_to.alert.accept()
driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()
