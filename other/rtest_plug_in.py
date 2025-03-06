import pytest
from time import sleep


class TestPlugIn:

    def test_plug_case_01(self):
        sleep(3)
        print('plug第一个用例')

    def test_plug_case_02(self):
        sleep(3)
        print('plug第二个用例')

    def test_plug_case_03(self):
        sleep(3)
        print('plug第三个用例')


if __name__ == '__main__':
    pytest.main(['-n 3'])
