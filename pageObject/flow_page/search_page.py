from time import sleep
import allure
from selenium.webdriver.common.by import By

from util_tools.basePage import BasePage


class SearchPage(BasePage):
    url = '/search.php'
    # 高级搜索按钮
    advanced_search = (By.LINK_TEXT, '高级搜索')
    # 关键词搜索框
    keywords = (By.NAME, 'keywords')
    # 立即搜索按钮
    submit = (By.NAME, 'Submit')
    # 购买按钮
    buy_button = (By.LINK_TEXT, '购买')

    def add_cart(self):
        """
        点击购买按钮将商品加入购物车中
        :return:
        """
        self.open_url(self.url)
        allure.attach(self.url, '打开测试页面', attachment_type=allure.attachment_type.TEXT)
        # 点击高级搜索
        self.click(self.advanced_search)
        # 搜索框输入数据
        self.send_keys(self.keywords, '二锅头')
        self.click(self.submit)
        sleep(2)
        allure.attach(self.screenshots_png(), '首页搜索框输入截屏', attachment_type=allure.attachment_type.PNG)
        # 点击购买按钮
        self.click(self.buy_button)
