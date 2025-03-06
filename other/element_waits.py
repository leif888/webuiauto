from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.leafground.com/select.xhtml")

# 强制等待
# sleep(5)
# ele = driver.find_element(By.ID, 'j_idt87:country_label')
# print(ele)

# 显示等待
# 等待元素可见
element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "j_idt87:country_label"))
)

# 隐式等待
driver.implicitly_wait(10)  # 设置隐式等待时间为10s

driver.find_element(By.ID, 'j_idt87:city_label')
driver.find_element(By.ID, 'j_idt87:country_label')

sleep(3)
