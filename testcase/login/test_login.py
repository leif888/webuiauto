import allure
import pytest

from pageObject.login_page.login_page import LoginPage
# from util_tools.handle_data.operateExcel import ExcelDataReader
# from util_tools.handle_data.readYaml import read_yaml
from util_tools.handle_data.operateJson import read_json


@allure.feature('登录模块')
class TestLogin:

    @allure.story('用户登录成功')
    @allure.title('登录成功')
    @allure.link(url='http://www.baidu.com', name='百度')
    @allure.description('测试用例的描述信息')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('data', read_json('./data/login_success.json'))
    def test_login_success(self, not_login_driver, data):
        username, password = data
        login_page = LoginPage(not_login_driver)
        login_page.login(username, password)
        allure.attach('这是一个附件内容', name=r'截图', attachment_type=allure.attachment_type.TEXT)
        # 断言结果
        login_page.assert_is_element_present(login_page.assert_result)

        # sleep(1)

    @allure.story('用户登录失败')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize('data', read_json('./data/login_failed.json'))
    def test_login_failed(self, not_login_driver, data):
        username, password = data
        login_page = LoginPage(not_login_driver)
        login_page.login(username, password)
        # 断言结果
        login_page.assert_title('系统提示')

        # sleep(1)

    # @pytest.mark.parametrize('data', read_yaml('./data/login.yaml'))
    # def test_login_success(self, get_driver, data):
    #     username, password = data
    #     login_page = LoginPage(get_driver)
    #     login_page.login(username, password)
    #
    #     # 断言结果
    #     success_ele = get_driver.find_element(By.XPATH, '//*[@id="ECS_MEMBERZONE"]/font/font')
    #     assert success_ele != ''
    #     sleep(3)

    # @pytest.mark.parametrize('data', ExcelDataReader('./data/login_testdata.xlsx').read_multiple_rows())
    # def test_login_success(self, get_driver, data):
    #     username, password = data
    #     login_page = LoginPage(get_driver)
    #     login_page.login(username, password)
    #
    #     # 断言结果
    #     success_ele = get_driver.find_element(By.XPATH, '//*[@id="ECS_MEMBERZONE"]/font/font')
    #     assert success_ele != ''
    #     sleep(3)
