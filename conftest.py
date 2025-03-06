import time

import pytest

from config.setting import is_dd_msg
from util_tools.connectMysql import ConnectMysql
from util_tools.dingRebot import send_dd_msg
from util_tools.logs_util.recordlog import logs


@pytest.fixture(scope='session', autouse=True)
def data_cleaning():
    """测试结束后清理测试数据"""
    conn = ConnectMysql()
    yield
    logs.info('正在清理测试数据...')
    sql = "delete from ecs_users where user_name='admin02'"
    conn.delete(sql)


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """pytest预定义的钩子函数，用于自动收集测试结果"""
    total = terminalreporter._numcollected
    passed = len(terminalreporter.stats.get('passed', []))
    failed = len(terminalreporter.stats.get('failed', []))
    error = len(terminalreporter.stats.get('error', []))
    skipped = len(terminalreporter.stats.get('skipped', []))
    duration = round(time.time() - terminalreporter._sessionstarttime, 2)
    summary = f"""
    自动化测试结果，通知如下，具体执行结果如下：
    测试用例总数：{total}
    测试通过数：{passed}
    测试失败数：{failed}
    错误数量：{error}
    跳过执行数量：{skipped}
    执行总时长：{duration}s
    """
    print(summary)
    if is_dd_msg:
        send_dd_msg(summary)
