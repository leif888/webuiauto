from selenium.webdriver.common.by import By
import allure
from util_tools.basePage import BasePage


# 登录页面类
class LoginPage(BasePage):
    url = '/user.php'
    # 用户名
    username = (By.NAME, 'username')
    # 密码
    password = (By.NAME, 'password')
    # 登录按钮
    submit = (By.NAME, 'submit')
    # 断言结果
    assert_result = (By.XPATH, '//*[@id="ECS_MEMBERZONE"]/font/font')

    # 登录操作
    def login(self, user_name, pass_word):
        self.open_url(self.url)
        allure.attach(self.url, '打开登录测试页面', attachment_type=allure.attachment_type.TEXT)
        # 输入用户名
        self.send_keys(self.username, user_name)
        # 输入密码
        self.send_keys(self.password, pass_word)
        # 点击登录按钮
        self.click(self.submit)
        allure.attach(self.screenshots_png(), f'{user_name}:输入内容截屏', attachment_type=allure.attachment_type.PNG)
