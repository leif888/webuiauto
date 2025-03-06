import pytest


class TestAssert:

    # 相等断言
    def test_case01(self):
        assert 1 == 2

    # 不相等断言
    def test_case02(self):
        assert 1 != 2

    # 真假断言
    def test_case03(self):
        assert_bool = False
        assert assert_bool is True

    # 成员关系断言
    def test_case04(self):
        container = ['pytest', 'unittest', 'python']
        item = 'python'
        assert item in container

    # 集合断言
    def test_case05(self):
        set_a = {1, 2, 3, 4}
        set_b = {4, 3, 2, 1}
        assert set_a == set_b


if __name__ == '__main__':
    pytest.main(['-vs'])
