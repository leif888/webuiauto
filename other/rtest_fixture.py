import pytest


# @pytest.fixture
# def init_browser(request):
#     print('前置操作，初始化浏览器对象')
#
#     def teardown():
#         print('后置操作，关闭浏览器对象，清理数据')
#
#     request.addfinalizer(teardown)  # 将teardown函数注册为最终器，以确保在测试用例运行结束后执行后置操作
#     return teardown


@pytest.fixture(scope='class', autouse=True)
def init_browser():
    print('前置操作，初始化浏览器对象')
    yield
    print('后置操作，关闭浏览器对象，清理数据')


@pytest.fixture(params=['apple', 'banana', 'orange'], ids=['苹果', '香蕉', '橘子'], name='setup_init')
def setup(request):
    value = request.param
    return value


class TestFixture:

    # 如果前置函数@pytest.fixture不带参数时，需要手动使用前置
    def test_case_01(self):
        print('fixture第一个测试用例')

    def test_case_02(self):
        print('fixture第二个测试用例')

    def test_case_03(self, setup_init):
        assert len(setup_init) > 0
