from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# webDriver初始化
driver = webdriver.Chrome()

# 页面导航
driver.get('https://www.leafground.com/frame.xhtml')

# 通过索引的方式切换到第一个iframe
driver.switch_to.frame(0)
# 在定位iframe内嵌框架里面的元素
driver.find_element(By.XPATH, '//*[@id="Click"]').click()

# 切换到父窗口（退出内嵌框架）
driver.switch_to.default_content()


sleep(4)