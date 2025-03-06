from time import sleep
import allure
from selenium.webdriver.common.by import By

from util_tools.basePage import BasePage


# 购物车页面
class FlowPage(BasePage):
    url = '/flow.php'
    # 结算中心按钮
    settle_button = (By.XPATH, '//*[@alt="checkout"]')
    # 继续购物按钮
    continue_button = (By.XPATH, '//*[@alt="continue"]')
    # 收货人信息-配送区域
    country = (By.NAME, 'country')
    province = (By.NAME, 'province')
    city = (By.NAME, 'city')
    district = (By.NAME, 'district')
    # 收货人信息
    consignee = (By.NAME, 'consignee')
    # 详细地址
    address = (By.NAME, 'address')
    # 电话
    tel = (By.NAME, 'tel')
    # 邮箱
    email = (By.NAME, 'email')
    # 配送至这个地址
    submit = (By.NAME, 'Submit')
    # 配送方式
    shipping_radio = (By.NAME, 'shipping')
    # 选择支付方式
    payment_radio = (By.NAME, 'payment')
    # 提交订单
    submit_order = (By.XPATH, '//input[@type="image"]')

    def flow_failed(self):
        """点击结算中心，购物车没有商品的情况下"""
        self.open_url(self.url)
        self.click(self.settle_button)

    def flow_success(self):
        """点击结算中心，购物车有商品"""
        self.open_url(self.url)
        allure.attach(self.url, '打开测试页面', attachment_type=allure.attachment_type.TEXT)
        self.click(self.settle_button)
        if self.is_element_present(self.country):
            # 选择配送区域
            self.selects(self.country, 1)
            self.selects(self.province, 3)
            self.selects(self.city, 5)
            self.selects(self.district, 2)
            # 输入收货人姓名
            self.send_keys(self.consignee, '张三')
            self.send_keys(self.address, '西三环南路72号院')
            self.send_keys(self.tel, '13922338989')
            self.send_keys(self.email, '2728@qq.com')
            sleep(2)
            allure.attach(self.screenshots_png(), '配送信息输入截屏', attachment_type=allure.attachment_type.PNG)
            self.click(self.submit)
        # 选择配送方式
        self.click(self.shipping_radio)
        # 选择支付方式
        self.click(self.payment_radio)
        sleep(2)
        # 提交订单
        self.click(self.submit_order)
        allure.attach(self.screenshots_png(), '提交订单页面截屏', attachment_type=allure.attachment_type.PNG)
