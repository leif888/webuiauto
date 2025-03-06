from time import sleep

import allure
from selenium.webdriver.common.by import By

from util_tools.basePage import BasePage


class FilesUploadPage(BasePage):
    """文件上传"""
    url = 'https://www.leafground.com/file.xhtml'
    # 文件选择
    files_input = (By.XPATH, '//*[@id="j_idt88:j_idt89_input"]')
    # 断言结果
    assert_result = (By.XPATH, '//*[@id="j_idt88:j_idt89"]/span[2]')

    def files_upload(self):
        self.open_url(self.url)
        allure.attach(self.url, '打开测试页面', attachment_type=allure.attachment_type.TEXT)
        # 设置要上传的文件路径
        file_path = r'C:\Users\yaozm\Desktop\文件上传.txt'
        allure.attach(file_path, '上传文件', attachment_type=allure.attachment_type.TEXT)
        # 上传文件
        self.send_keys(self.files_input, file_path)
        allure.attach(self.screenshots_png(), '文件上传截屏', attachment_type=allure.attachment_type.PNG)
        sleep(2)
