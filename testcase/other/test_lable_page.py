import allure

from pageObject.other.label_page import LabelPage


@allure.feature('浏览器打开新标签页')
class TestLabelPage:

    @allure.story('在新标签上继续操作')
    def test_open_new_label(self, not_login_driver):
        label_page = LabelPage(not_login_driver)
        label_page.open_new_table_operate()
