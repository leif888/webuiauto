from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 打开网页
driver.get('http://localhost/ecshop/user.php?act=register')

# ID元素定位
driver.find_element(By.ID, 'username')

# name属性定位
driver.find_element(By.NAME, 'username')

# class_name元素定位
driver.find_element(By.CLASS_NAME, 'inputBg')

# tag_name元素定位
driver.find_element(By.TAG_NAME, 'input')

# css selector选择器元素定位
# 1）id选择器定位
driver.find_element(By.CSS_SELECTOR, '#username')

# 2）类选择器
driver.find_element(By.CSS_SELECTOR, '.inputBg')

# 3）标签选择器定位
driver.find_element(By.CSS_SELECTOR, 'input')  # 查找第一个<input>标签

# 4）属性选择器
driver.find_element(By.CSS_SELECTOR, '[type="text"]')  # 单个属性定位

driver.find_element(By.CSS_SELECTOR, '[type="text"][id="username"]')  # 多个属性定位

driver.find_element(By.CSS_SELECTOR, 'input[class="inputBg"]')  # 标签名+属性选择器组合定位

driver.find_element(By.CSS_SELECTOR, 'input#username')  # 通过标签名+ID选择器组合定位

driver.find_element(By.CSS_SELECTOR, 'input.inputBg')  # 通过标签名+类选择器组合定位

driver.find_element(By.CSS_SELECTOR, 'table>tbody>tr')  # 通过标签层级定位

driver.find_element(By.CSS_SELECTOR, 'table>tbody>tr:first-child td:nth-child(2) input[type="text"]')  # 表格层级定位

# 5）模糊定位

# 6）link_text 完整超链接文本定位
driver.find_element(By.LINK_TEXT, '我已有账号，我要登录')

# 7）partial_link_text 部分超链接文本定位
driver.find_element(By.PARTIAL_LINK_TEXT, '我已有账号')

# 8）Xpath定位方式
# 8.1）使用绝对路径定位
driver.find_element(By.XPATH, '/html/body//input[@name="username"]')

# 8.2）使用相对路径定位
driver.find_element(By.XPATH, '//input[@name="username"]')

# 8.3）通过文本内容定位，关键字函数：text()
driver.find_element(By.XPATH, '//*[text()="我已有账号，我要登录"]')

# 8.4）通过部分文本内容定位，模糊匹配，关键字函数：contains()
driver.find_element(By.XPATH, '//*[contains(text(),"我已有账号")]')

# 8.5）通过元素属性来定位
driver.find_element(By.XPATH, '//*[@name="username"]')

# 8.6）使用逻辑运算符定位
driver.find_element(By.XPATH, '//*[@name="username" and @id="username"]')

# 8.7）使用函数
driver.find_element(By.XPATH, '//input[contains(@id,"username")]').send_keys('测试')

sleep(3)
