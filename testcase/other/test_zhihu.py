from pageObject.other.zhihu_page import ZhiHuPage


class TestZhiHu:

    def test_write_content(self, not_login_driver):
        zh = ZhiHuPage(not_login_driver)
        zh.write_content()
