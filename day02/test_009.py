'''
fixture嵌套
'''
import random

# 生成用户名
import pytest
import requests

'''
@pytest.fixture()
def get_username():
    return "admin" + str(random.randint(1,1000))

# 生成密码
@pytest.fixture()
def get_pwd():
    return random.randint(10000,999999999)

@pytest.fixture()
def get_login_data(get_username,get_pwd):
    return {"username":get_username,"pwd":get_pwd}
print(get_login_data)
def test_login(get_login_data):
    print(f"测试登录用例，登录数据为：{get_login_data}")
'''


cs = [
    # 登录成功用例
    {'data':{'mobilenumber': '18312345678','pwd': '123456'},
     'code':'20103'},
    # 密码长度为5
    {'data':{'mobilenumber': '18312345678','pwd': '12345'},
     'code':'20103'},
    # 密码成都为19
    {'data': {'mobilenumber': '18312345678', 'pwd': '1234512345123451234'},
     'code': '20103'},
    # 密码成都为19
    {'data': {'mobilenumber': '18312345678', 'pwd': '1234512345123451234'},
     'code': '20103'},
    # 手机号码为空
    {'data': {'mobilenumber': '', 'pwd': '123456'},
     'code': '20103'},
    ]

@pytest.fixture(params=cs)
def login_data(request):
    return request.param


def login(data):
    url='http://jy001:8081/futureloan/mvc/api/member/login'
    r = requests.post(url,data=data)
    return r

# 数据驱动测试模型
def test_login_data(login_data):
    print(f"测试数据：{login_data['data']}")
    print(f"预期结果：code={login_data['code']}")
    r = login(login_data['data'])
    print(f"实际结果:{r.text}")

    assert r.json()['code'] ==login_data['code']
