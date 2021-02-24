import pytest

from Zonghe.baw import Member
from Zonghe.caw import DataRead, MysqlOP


# 登录前置（注册）数据
@pytest.fixture(params=DataRead.read_yaml(r"test_data/login_setup.yaml"))
def setup_data(request):
    return request.param


# 登录数据
@pytest.fixture(params=DataRead.read_yaml(r"test_data/login_data.yaml"))
def login_data(request):
    return request.param


@pytest.fixture()
def regiter(setup_data,baserequest,url,db_info):
    # 初始化环境
    MysqlOP.delete_user(db_info,setup_data['data']['mobilephone'])
    # 注册用户
    r = Member.register(baserequest,url,setup_data['data'])
    yield
    # 清理环境，删除用户
    MysqlOP.delete_user(db_info,setup_data['data']['mobilephone'])


def test_login(regiter,baserequest,url,login_data):
    # 下发登录请求
    r = Member.login(baserequest,url,data=login_data['data'])
    # 检查结果
    assert r.json()['code'] == login_data['expect']['code']
    assert r.json()['status'] == login_data['expect']['status']
    assert r.json()['msg'] == login_data['expect']['msg']