from time import sleep

import allure
from selenium.webdriver.common.by import By

from util_tools.basePage import BasePage


class LabelPage(BasePage):
    """点击后打开新的标签页，然后在新的标签页上继续操作"""
    url = 'https://www.leafground.com/window.xhtml'
    # 点击按钮
    click_button = (By.XPATH, '//*[@id="j_idt88:new"]/span')
    # 新的标签页，邮箱地址输入框
    email_address = (By.ID, 'email')
    # 邮箱内容
    message = (By.ID, 'message')
    # 新标签页的url
    label_new_url = 'https://www.leafground.com/dashboard.xhtml'

    def open_new_table_operate(self):
        self.open_url(self.url)
        allure.attach(self.url, '打开测试页面', attachment_type=allure.attachment_type.TEXT)
        self.click(self.click_button)
        sleep(3)
        # 打开新标签页的url
        # self.open_url(self.label_new_url)
        self.switch_to_new_tab()
        allure.attach('切换新的标签页', '打开新的标签页', attachment_type=allure.attachment_type.TEXT)
        # 在新标签页进行操作
        self.send_keys(self.email_address, '673889@163.com')
        self.send_keys(self.message, 'selenium窗口句柄切换')
        allure.attach(self.screenshots_png(), '邮箱地址和内容输入截屏', attachment_type=allure.attachment_type.PNG)
        sleep(2)
