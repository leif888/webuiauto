from selenium.webdriver.common.by import By
import allure
from util_tools.basePage import BasePage


# 注册页面类
class RegisterPage(BasePage):
    url = '/user.php?act=register'
    # 用户名
    username = (By.NAME, 'username')
    # email
    email = (By.NAME, 'email')
    # 密码
    password = (By.NAME, 'password')
    # 确认密码
    confirm_password = (By.ID, 'conform_password')
    # MSN
    msn = (By.NAME, 'extend_field1')
    # QQ
    qq = (By.NAME, 'extend_field2')
    # 办公电话
    office_phone = (By.NAME, 'extend_field3')
    # 家庭电话
    family_phone = (By.NAME, 'extend_field4')
    # 手机
    phone = (By.NAME, 'extend_field5')
    # 密码提示问题
    select = (By.NAME, 'sel_question')
    # 密码问题答案
    passwd_answer = (By.NAME, 'passwd_answer')
    # 立即注册按钮
    submit_button = (By.NAME, 'Submit')
    # 断言结果定位
    assert_result = (By.XPATH, '/html/body/div[7]/div[2]/div/div/div/font')
    # 断言用户已存在的结果
    assert_user_exist = (By.XPATH, '//*[@id="username_notice"]')
    # 跳转登录按钮
    skip_login_button = (By.PARTIAL_LINK_TEXT, '我要登录')

    def click_register(self, user_name, email, passwd, confirm_passwd, msn, qq, office_phone, family_phone, phone,
                       passwd_answer):
        # 打开被测页面
        self.open_url(self.url)
        allure.attach(self.url, '打开测试页面', attachment_type=allure.attachment_type.TEXT)
        # 依次在输入项输入内容
        self.send_keys(self.username, user_name)
        self.send_keys(self.email, email)
        self.send_keys(self.password, passwd)
        self.send_keys(self.confirm_password, confirm_passwd)
        self.send_keys(self.msn, msn)
        self.send_keys(self.qq, qq)
        self.send_keys(self.office_phone, office_phone)
        self.send_keys(self.family_phone, family_phone)
        self.selects(self.select, 3)
        self.send_keys(self.phone, phone)
        self.send_keys(self.passwd_answer, passwd_answer)
        # 点击立即注册按钮
        self.click(self.submit_button)
        allure.attach(self.screenshots_png(), '注册页面截屏', attachment_type=allure.attachment_type.PNG)

    def skip_login_page(self):
        self.open_url(self.url)
        self.click(self.skip_login_button)
