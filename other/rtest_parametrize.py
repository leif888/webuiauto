import pytest


class TestParams:

    @pytest.mark.parametrize("params", ['python', 'java', 'C#'])
    # 参数化单个参数
    def test_params_01(self, params):
        print(params)

    @pytest.mark.parametrize("username,password,address",
                             [("test01", "qwe123", 'BJ'), ("test02", "qwe456", 'CD'), ("test03", "qwe789", 'NC')])
    # 参数化多个参数，使用列表可迭代对象进行参数化
    def test_login_case(self, username, password, address):
        print(f"用户名：{username},密码：{password},地址：{address}")

    @pytest.mark.parametrize("username,password", {("test01", "qwe123"), ("test02", "qwe456"), ("test03", "qwe789")})
    # 使用集合可迭代对象进行参数化
    def test_login_case_02(self, username, password):
        print(f"用户名：{username},密码：{password}")

    @pytest.mark.parametrize("user_name", {"test01": "qwe123", "test02": "qwe456"})
    # 使用字典可迭代对象进行参数化
    def test_login_case_03(self, user_name):
        print(f"用户名：{user_name}")
