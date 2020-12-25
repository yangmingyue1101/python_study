# -*-coding:UTF-8 -*-
from time import sleep
from pymysql import connect
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

class Testgoods():
    def login(self):
        driver=webdriver.Chrome()
        driver.get('http://192.168.1.4/ecshop/admin/privilege.php?act=login')
        driver.maximize_window()
        driver.find_element_by_name('username').send_keys('caichang')
        driver.find_element_by_name('password').send_keys('caichang1')
        driver.find_element_by_class_name('btn-a').click()
        return driver
    def into(self):
        driver=self.login()
        driver.switch_to.frame('menu-frame')
        driver.find_element_by_link_text('商品列表').click()
        driver.switch_to.default_content()
        driver.switch_to.frame('main-frame')
        return driver
    def get_connect(self):
        conn=connect('192.168.1.4','root','root','ecshop',3306)
        return conn
    def get_cursor(self):
        cursor=self.get_connect().cursor()
        return cursor
    def test_search(self):
        driver=self.into()
        sleep(2)
        driver.find_element_by_name('keyword').send_keys('车')
        driver.find_element_by_xpath("//input[@value=' 搜索 ']").click()
        sleep(2)
        try:
            web_result=driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span').text
            web_pages=driver.find_element_by_id('totalRecords').text
            cursor=self.get_cursor()
            cursor.execute("select goods_name from ecs_goods where goods_name like'%车%'")
            result=cursor.fetchall()
    #         print(result[0][0])
            cursor.execute("select count(*) from ecs_goods where goods_name like'%车%'")
            total_page=cursor.fetchall()
    #         print(total_page[0][0])
            assert web_result==result[0][0] and int(web_pages) == total_page[0][0]
        except NoSuchElementException:
            print('对不起，没有数据，无法执行删除操作')   
            cursor.close()
            self.get_connect().close()
            driver.close()
            
    def test_add(self):
        driver=self.login()
        driver.switch_to.frame('menu-frame')
        driver.find_element_by_link_text('添加新商品').click()
        driver.switch_to.default_content()
        driver.switch_to.frame('main-frame')
        sleep(2)
        driver.find_element_by_name('goods_name').send_keys('小米手机')
        Select(driver.find_element_by_name('cat_id')).select_by_visible_text('    小型手机')
        driver.find_element_by_xpath("//input[@value=' 确定 ']").click()
        
        cursor=self.get_cursor()
        cursor.execute('select goods_name from ecs_goods where goods_name=\'小米手机\'')
        aa=cursor.fetchone()
        assert aa[0]=='小米手机'
           
        
        cursor.close()
        self.get_connect().close()
        driver.close()
    def test_isonsale(self): 
        driver=self.into()
        goods_name=driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span').text
        img_type= driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[5]/img').get_attribute('src').split('/')
        # print(img_type)
        if img_type[-1]=='no.gif':
            is_on_sale=1
        else:
            is_on_sale=0
        
        driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[5]/img').click()
        
        cursor=self.get_cursor()
        cursor.execute("select is_on_sale from ecs_goods where goods_name='%s'" %goods_name)
        result=cursor.fetchone()
        assert result[0]==is_on_sale
        cursor.close()
        self.get_connect().close()
        driver.close()
            
