import pytest

from util_tools.logs_util.recordlog import logs


@pytest.fixture(autouse=True)
def info_output():
    logs.info('----测试用例开始执行----')
    yield
    logs.info('----测试用例执行完毕----')
