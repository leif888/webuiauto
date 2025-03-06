import pytest


class TestReRunFailed:

    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 对单个测试用例设置失败重跑次数
    def test_rerun_fail_case(self):
        import random
        assert random.choice([True, False])

    def test_rerun_fail_case02(self):
        import random
        assert random.choice([True, False])


if __name__ == '__main__':
    pytest.main(['--reruns=3'])
