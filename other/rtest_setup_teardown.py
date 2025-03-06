class TestSetupTeardown:

    def setup(self):
        print('执行测试用例前先执行前置操作')

    def test_case_01(self):
        print('第一个测试用例')

    def test_case_02(self):
        print('第二个测试用例')

    def test_case_03(self):
        print('第三个测试用例')

    def teardown(self):
        print('执行测试用例后执行后置操作')
