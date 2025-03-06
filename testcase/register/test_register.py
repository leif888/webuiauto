from time import sleep

import allure
import pytest

from pageObject.register_page.register_page import RegisterPage
from util_tools.handle_data.readYaml import read_yaml


@allure.feature('注册模块')
class TestRegister:

    @allure.story('注册成功场景')
    @pytest.mark.parametrize('data', read_yaml('./data/register_success.yaml'))
    def test_register_success(self, not_login_driver, data):
        register_page = RegisterPage(not_login_driver)
        # 如果使用*data解包数据，data的元素数量必须跟click_register方法的入参个数保持一致
        register_page.click_register(*data)
        sleep(2)
        # 断言结果
        register_page.assert_is_element_present(register_page.assert_result)

    @allure.story('注册失败的场景')
    @pytest.mark.parametrize('data', read_yaml('./data/register_failed.yaml'))
    def test_register_failed(self, not_login_driver, data):
        register_page = RegisterPage(not_login_driver)
        # 如果使用*data解包数据，data的元素数量必须跟click_register方法的入参个数保持一致
        register_page.click_register(*data)
        sleep(2)
        # 断言结果
        register_page.assert_element_not_visible(register_page.assert_result)

    @allure.story('注册页面成功跳转到登录页面')
    def test_check_skip_login(self, not_login_driver):
        register_page = RegisterPage(not_login_driver)
        register_page.skip_login_page()
        # 断言结果
        assert register_page.current_url == 'http://localhost/ecshop/user.php?act=login'
