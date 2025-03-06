from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# webDriver初始化
driver = webdriver.Chrome()

# 页面导航
# driver.get('http://localhost/ecshop/user.php?act=register')
# driver.get('https://www.leafground.com/radio.xhtml')
driver.get('https://www.leafground.com/input.xhtml')

# 窗口最大化
driver.maximize_window()

# 查找元素
# driver.find_element(By.ID, 'username')

# 与元素交互，在网页上执行各种操作
# driver.find_element(By.NAME, 'email').send_keys('123456@163.com')  # 输入文本函数
# driver.find_element(By.XPATH, '//input[@name="Submit"]').click()  # 点击函数

# 下拉框的处理
# sel = Select(driver.find_element(By.NAME, 'sel_question'))
# sel.select_by_index(3) # 通过下拉选项的索引去获取
# sel.select_by_value('favorite_movie') # 通过下拉选项标签的value值定位
# sel.select_by_visible_text('我最大的爱好？')  # 通过下拉选项的标签的文本内容定位
#
# sel.deselect_by_index(2)  # 当下拉选项多选的情况下，通过索引取消选择
# sel.deselect_by_value('favorite_movie')  # 通过标签的value值取消选择
# sel.deselect_by_visible_text('我最大的爱好？')  # 通过标签文本取消选择
# sel.deselect_all()  # 取消全部下拉选项

# 警告框的处理
# alert = driver.switch_to.alert
# sleep(3)
# alert.accept()

# 单选按钮的处理
# driver.find_element(By.XPATH, '//*[@id="j_idt87:console1"]/tbody/tr/td[4]/label').click()

# 滑动条拖动的处理
# 定位到进度条的滑块元素
slider = driver.find_element(By.ID, 'j_idt106:j_idt120')
# 获取滑块元素的大小
slider_width = slider.size['width']
# 计算要拖动的偏移量（比如说，要拖动到一半的位置）
offset = slider_width / 8
# 使用ActionChains进行拖动操作
action = ActionChains(driver)
# click_and_hold：点击并保持住滑块元素，准备拖动；move_by_offset：通过指定的偏移量来移动滑块；
# release：释放鼠标，完成拖动操作；perform：执行以上定义的动作链
action.click_and_hold(slider).move_by_offset(offset, 0).release().perform()

# 文本框实现自增或自减操作
number_input = driver.find_element(By.ID, 'j_idt106:j_idt118_input')
# 清空输入框
number_input.clear()
# 手动输入新的值
number_input.send_keys("10")
# 使用文本框上的向上箭头模拟值自增
number_input.send_keys(Keys.ARROW_UP)
sleep(2)
# 使用文本框上的向下箭头模拟值自减
number_input.send_keys(Keys.ARROW_DOWN)

# 文本框弹出日期选择的处理
# 定位到文本框
date_input = driver.find_element(By.ID, 'j_idt106:j_idt116_input')
# 触发文本框的点击事件，弹出日期选择框
date_input.click()
# 定位到弹出的日期选择框里面的元素
date_element = driver.find_element(By.XPATH, '//*[@id="j_idt106:j_idt116_panel"]/div/div[2]/table/tbody/tr[5]/td[7]/a')
date_element.click()

# 页面截图
driver.save_screenshot('scr.png')

sleep(5)
