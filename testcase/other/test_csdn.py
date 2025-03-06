from pageObject.other.csdn_page import CSDNPage


class TestCSDN:

    def test_csdn_write(self, not_login_driver):
        csdn = CSDNPage(not_login_driver)
        csdn.publish_an_article()
