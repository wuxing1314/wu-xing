'''
fixture级别：
    session
    class
    function(默认)
    mudule
'''
import pytest

@pytest.fixture(scope = 'module')
def db():
    print("前置：连接数据库")
    yield
    print("后置：断开数据库")

@pytest.fixture(scope = 'module')
def login():
    print("前置：是在首次调用login的地方执行")
    yield
    print("后置：模块所有用例执行完后执行后置")

def test_001():
    print("用例1")

def test_002(db,login):  #这个用例执行前置
    print("用例2")

def test_003():
    print("用例3")

def test_004():  # 这个用例执行后置
    print("用例4")