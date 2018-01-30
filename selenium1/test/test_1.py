from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
print(time.strftime('%Y-%m-%d %H:%M:%S'))
#前提条件
#1.驱动
#2.selenium
#3.ping 127.0.0.1
driver = webdriver.Chrome()
print(time.strftime('%Y-%m-%d %H:%M:%S'))

driver.get("http://10.208.2.10:8001/web/")
#登录
text_box_user = driver.find_element_by_id("userAccount")
text_box_user_pwd = driver.find_element_by_name("userPassword")
text_box_user.send_keys("zqf")
text_box_user_pwd.send_keys("1111")
text_box_user.submit()
#切换主题
driver.execute_script('switch2NewTheme()')#触发javascript
result = EC.alert_is_present()(driver)#获取弹窗
print(result.text)#打印弹窗内容
result.accept()#弹窗确认