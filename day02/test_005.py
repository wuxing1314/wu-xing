'''
fixture级别：
    session
    class
    function(默认)
    mudule
'''

import pytest

@pytest.fixture(scope = 'class')
def db():
    print("前置：类里连接数据库")
    yield
    print("后置：类里断开数据库")

@pytest.fixture(scope = 'class')
def login():
    print("前置：在类里是在首次调用login的地方执行")
    yield
    print("后置：类里模块所有用例执行完后执行后置")

class TestRegister:

    def test_001(self):
        print("注册用例1")

    def test_002(self,db):  #类里这个用例执行前置
        print("注册用例2")

    def test_003(self):
        print("注册用例3")



class TestLogin:

    def test_001(self):
        print("登录用例1")

    def test_002(self,login):  # 类里这个用例执行前置
        print("登录用例2")

    def test_003(self):
        print("登录用例3")