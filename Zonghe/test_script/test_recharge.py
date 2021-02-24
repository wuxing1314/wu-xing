'''
充值测试
'''
import pytest

from Zonghe.baw import Member
from Zonghe.caw import DataRead, MysqlOP, Check


# 获取测试数据
@pytest.fixture(params=DataRead.read_yaml("test_data/recharge.yaml"))
def recharge_data(request):
    return request.param

def test_recharge(recharge_data,baserequest,url,db_info):
    # 初始换环境
    MysqlOP.delete_user(db_info,recharge_data['register']['mobilephone'])
    # 注册用户
    Member.register(baserequest,url,recharge_data['register'])
    # 充值
    r = Member.recharge(baserequest,url,recharge_data['data'])
    # 断言验证
    Check.equal(r.json(),recharge_data['expect'],'code,msg,status')
    # 恢复初始化环境
    MysqlOP.delete_user(db_info, recharge_data['register']['mobilephone'])