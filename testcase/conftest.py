import allure
import pytest
from selenium import webdriver

from config.setting import browser_type, WAIT_TIME
from pageObject.login_page.login_page import LoginPage
from util_tools.logs_util.recordlog import logs


@pytest.fixture(autouse=True)
def log_outputs():
    logs.info('-------测试用例开始执行-------')
    yield
    logs.info('-------测试用例执行完毕-------')


def init_driver():
    # 初始化浏览器对象
    browser_mapping = {
        'Chrome': webdriver.Chrome,
        'Edge': webdriver.Edge,
        'Firefox': webdriver.Firefox
    }
    if browser_type.capitalize() in browser_mapping:
        return browser_mapping.get(browser_type.capitalize())()


@pytest.fixture(scope='class')
def get_driver():
    driver = init_driver()
    # 设置一个全局的隐式等待时间
    driver.implicitly_wait(WAIT_TIME)
    # 最大化浏览器窗口
    # driver.maximize_window()
    yield driver
    driver.quit()


# 登录状态的前置应用
@pytest.fixture(scope='class')
def login_driver(get_driver):
    driver = get_driver
    login_page = LoginPage(driver)
    login_page.login('admin123', '123456')
    return driver


# 未登录状态的前置应用
@pytest.fixture()
def not_login_driver():
    global driver
    driver = init_driver()
    driver.implicitly_wait(WAIT_TIME)
    # 最大化浏览器窗口
    driver.maximize_window()
    yield driver
    driver.quit()


# 钩子函数,对失败测试用例进行截图
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    coucome = yield
    result = coucome.get_result()
    if result.when == 'call':
        xfail = hasattr(result, 'wasxfail')
        if (result.skipped and xfail) or (result.failed and not xfail):
            with allure.step('测试用例失败截图'):
                allure.attach(driver.get_screenshot_as_png(), '失败截图', attachment_type=allure.attachment_type.PNG)
