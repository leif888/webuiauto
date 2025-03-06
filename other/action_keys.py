from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

# driver.get("https://www.leafground.com/input.xhtml")
driver.get("https://www.leafground.com/select.xhtml")

# 定位到多行文本框
# lines_element = driver.find_element(By.ID, 'j_idt88:j_idt101')
# lines_element.send_keys('多行文本框第一行')
# # 模拟键盘回车键
# ActionChains(driver).send_keys(Keys.ENTER).perform()
# lines_element.send_keys('第二行文字')

# 模拟鼠标的操作
# 1）点击
# driver.find_element(By.ID, 'j_idt88:j_idt101').click()
# 2）右键点击，context_click
# ele = driver.find_element(By.ID, 'j_idt88:j_idt101')
# ActionChains(driver).context_click(ele).perform()
# 3）双击，double_click
# double_ele = driver.find_element(By.ID, 'j_idt88:j_idt91')
# ActionChains(driver).double_click(double_ele).perform()
# 4）鼠标悬停，move_to_element
# move_element = driver.find_element(By.XPATH, '//*[@id="menuform:j_idt40"]/a')
# ActionChains(driver).move_to_element(move_element).perform()
# 5）拖拽操作，drag_and_drop
# source = driver.find_element(By.ID, 'source')
# target = driver.find_element(By.ID, 'target')
# ActionChains(driver).drag_and_drop(source, target).perform()

# 6）鼠标滚动
# 使用JavaScript来执行向下滚动到页面底部
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

# 下拉菜单有多个选项，模拟鼠标滚动到最底部那个，并点击选择
dropdown = driver.find_element(By.ID, 'j_idt87:lang_label')
dropdown.click()
# 模拟鼠标滚轮向下滚动
for _ in range(8):
    ActionChains(driver).send_keys(Keys.DOWN).perform()

sleep(4)
