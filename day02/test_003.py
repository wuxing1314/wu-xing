'''
更灵活的一种前置后置的方法：fixture
    可以不用setup、teardown的命名方式
    使用更灵活
'''
import pytest

# 测试前置：测试之前的环境准备、环境初始化、测试数据等准备工作
# 测试后置，测试结束后环境恢复等
@pytest.fixture() # 作用域默认是function级别的；
def login():
    print("登录系统")
    yield  #yield之前是前置，之后是后置
    print("退出系统")
    print("测试结束")


def test_query():
    print("查询功能，不需要登录")

# 需要前置的地方，将login作为参数传入
def test_add(login):
    print("添加功能，需要登录")

# 需要前置的地方，使用pytest.mark.usefixtures()装饰器实现
@pytest.mark.usefixtures('login')
def test_delete():
    print("删除功能，需要登录")

def test_reister():
    print("注册功能，不需要登录")