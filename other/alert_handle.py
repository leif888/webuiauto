from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.leafground.com/alert.xhtml")

# alert警告框处理
driver.find_element(By.XPATH, '//*[@id="j_idt88:j_idt91"]/span[2]').click()
alert = driver.switch_to.alert
sleep(2)
alert.accept()  # 点击确定

# Alert (Confirm Dialog),有确定和取消按钮的弹框
driver.find_element(By.XPATH, '//*[@id="j_idt88:j_idt93"]/span[2]').click()
alert = driver.switch_to.alert
sleep(2)
# alert.accept()  # 点击确定
alert.dismiss()  # 点击取消

# Sweet Alert (Simple Dialog)，是一个自定义的弹框库
driver.find_element(By.XPATH, '//*[@id="j_idt88:j_idt95"]/span[2]').click()
# driver.switch_to.frame(0)
driver.find_element(By.XPATH, '//*[@id="j_idt88:j_idt98"]/span[2]').click()

# Sweet Modal Dialog,模态框处理
driver.find_element(By.XPATH, '//*[@id="j_idt88:j_idt100"]/span[2]').click()
driver.find_element(By.XPATH, '//*[@id="j_idt88:j_idt101"]/div[1]/a/span').click()


sleep(4)
