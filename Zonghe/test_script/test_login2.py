import pytest

from Zonghe.baw import Member
from Zonghe.caw import DataRead, MysqlOP, Check


@pytest.fixture(params=DataRead.read_yaml(r"test_data/login.yaml"))
def login_data(request):
    return request.param


def test_login(login_data,baserequest,url,db_info):
    # 创建初始环境
    MysqlOP.delete_user(db_info, login_data['register']['mobilephone'])
    # 注册用户
    r = Member.register(baserequest,url,login_data['register'])
    # 登录
    q = Member.login(baserequest,url,login_data['data'])
    # 检查结果
    '''
    assert q.json()['code'] == login_data['expect']['code']
    assert q.json()['status'] == login_data['expect']['status']
    assert q.json()['msg'] == login_data['expect']['msg']
    '''
    Check.equal(q.json(),login_data['expect'],'code,status,msg')
    # 恢复环境
    MysqlOP.delete_user(db_info,login_data['register']['mobilephone'])
