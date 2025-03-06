import pytest


class TestAddUser:

    @pytest.mark.P1
    def test_add_user_01(self):
        print('新增用户01')

    def test_add_user_02(self):
        print('新增用户02')

    @pytest.mark.P2
    def test_add_user_03(self):
        print('新增用户03')
