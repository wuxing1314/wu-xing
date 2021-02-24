'''
session级别的前置和后置，放到conftest.py 文件中，
不需要import pytest，根据文件名字找对应方法
脚本层的一些方法可以放到这里

一个工程可以包含多个conftest.py，conftest.py对同级目录以及该目录下的子目录生效
'''
import pytest


@pytest.fixture(scope = 'session')
def db():
    print("前置：连接数据库")
    yield
    print("后置：断开数据库")

@pytest.fixture(scope = 'session')
def login():
    print("前置：整个执行过程，在首次调用login的地方执行")
    yield
    print("后置：整个执行过程，在模块所有用例执行完后执行后置")