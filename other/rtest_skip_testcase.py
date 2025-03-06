import pytest


class TestSkipTestCase:

    def test_skip_case_01(self):
        print('第一个用例')

    sum = 5

    @pytest.mark.skipif(condition=sum == 5, reason="不符合条件")  # condition：表达式；reason：跳过执行的一个说明
    def test_skip_case_02(self):
        print('第二个用例')

    @pytest.mark.skip  # 无条件跳过执行
    def test_skip_case_03(self):
        print('第三个用例')

    def test_skip_case_04(self):
        print('第四个用例')

    @pytest.mark.xfail
    def test_xfail_case_05(self):
        a = 1
        b = 2
        assert a == b
