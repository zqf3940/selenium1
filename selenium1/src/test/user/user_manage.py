import os,sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))+"\\base")
from base_login import base_login
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

#用户管理测试
class user_manage(base_login):

    driver = webdriver.Chrome()
    base_login.getLoginIndex(driver)
    #隐形等待,防止未加载完成
    driver.implicitly_wait(5)
    menu_user = driver.find_element_by_xpath('//ul[@id="mainnav-menu"]/li[2]')
    menu_user.click()#打开用户管理菜单
