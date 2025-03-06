from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# 访问网页
driver.get('http://www.baidu.com')

# 元素定位，selenium3.0和selenium4.0的差异
# ele = driver.find_element_by_id('kw')  # 3.0写法
# print(ele)
# driver.find_element_by_name('wd')
# driver.find_element_by_class_name('s_ipt')
# driver.find_element_by_xpath('')

driver.find_element(By.ID, 'kw').send_keys('selenium4.0新特性')  # 4.0写法

# 打开新的窗口方式
driver.switch_to.new_window()

