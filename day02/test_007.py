'''
fixture带参数
'''
import pytest


@pytest.fixture(params =["root","admin","liulaoda"])  #代表不同用户名
def login_data(request): # 固定写法“request”，时pytest里边的关键字，不可更改
    return request.param # 固定写法"return request.param"

#使用3组数据登录
def test_login(login_data):
    print(login_data)
    # f时format,格式化的意思，等同于%s-->%login_data
    print(f"测试登录功能，使用用户名：{login_data}登录")

@pytest.fixture(params =[{"username":"root","pwd":"123456"},{"username":"admin","pwd":"123456"}])
def login_data1(request): # 固定写法“request”，时pytest里边的关键字，不可更改
    return request.param # 固定写法"return request.param"


def test_login1(login_data1):
    print(f"测试登录功能，使用用户名：{login_data1['username']},密码{login_data1['pwd']}登录")


@pytest.fixture(params =[("root","123456"),("admin","123456"),])
def login_data2(request): # 固定写法“request”，时pytest里边的关键字，不可更改
    return request.param # 固定写法"return request.param"


def test_login2(login_data2):
    print(f"测试登录功能，使用用户名：login_data1(0),密码login_data1(1)登录")