import os,sys,time
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))+"\\base")
from base_login import base_login
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

#门店管理测试
class mt_store(base_login):
    #循环用
    i = 0

    driver = webdriver.Chrome()
    base_login.getLoginIndex(driver)

    #隐形等待,防止未加载完成
    driver.implicitly_wait(10)
    time.sleep(1)#休眠一秒
    menu_user = driver.find_element_by_xpath('//ul[@id="mainnav-menu"]/li[3]')
    menu_user.click()#打开门店信息管理
    menu_user = driver.find_element_by_xpath('//ul[@id="mainnav-menu"]/li[3]/ul/li[1]')
    menu_user.click()#打开MT门店资料
    driver.implicitly_wait(10)
    time.sleep(1)#休眠一秒
    driver.switch_to.frame("main")#切换到主页面
    menu_user = driver.find_element_by_xpath('//div[@id="MenuList"]').find_element_by_link_text('新增')
    menu_user.click()#打开MT门店资料-新增
    driver.implicitly_wait(10)
    time.sleep(1)#休眠一秒

    #填写门店资料
    store_input = driver.find_elements_by_xpath('//table[@id="form6015_1"]/tbody/tr/td/input')
    for inp in store_input:
        if inp.get_attribute('type') == 'hidden':
            continue
        elif inp.get_attribute('readonly') == 'true':
            if i != 0:
                inp.click()
                inp.send_keys('test')
        else:
            print(inp.get_attribute('name'))
            inp.send_keys('tesform6015~1~7~pf_a6710572_3t')

        i+=1