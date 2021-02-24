'''
测试注册的脚本
'''

import pytest

from Zonghe.baw import Member
from Zonghe.caw import DataRead, MysqlOP


@pytest.fixture(params=DataRead.read_yaml(r"test_data/register_fail.yaml"))
def fail_data(request):
    return request.param

'''
@pytest.fixture(params=DataRead.read_yaml(r"test_data/login_data.yaml"))
def login_data(request):
    return request.param
'''



def test_register_fail(fail_data, baserequest, url):
    '''
    注册失败的脚本
    :return:
    '''
    # 下发请求
    # 校验结果
    # 打印数据 print(fail_data)

    r = Member.register(baserequest, url, fail_data['data'])

    print(r)
    # 断言
    assert r.json()['code'] == fail_data['expect']['code']
    assert r.json()['status'] == fail_data['expect']['status']
    assert r.json()['msg'] == fail_data['expect']['msg']


@pytest.fixture(params=DataRead.read_yaml(r"test_data/register_pass.yaml"))
def pass_data(request):
    return request.param


def test_register_pass(pass_data, baserequest, url, db_info,login_data):
    '''
    测试注册成功功能
    :param pass_data:
    :param baserequest:
    :param url:
    '''

    # 1、初始化环境：避免环境中已有本次测试用到的数据
    MysqlOP.delete_user(db_info, pass_data['data']['mobilephone'])

    # 2、调用注册方法，注册
    r = Member.register(baserequest, url, pass_data['data'])
    print(r)
    # 3、断言注册
    # 方法1：断言接口返回值
    assert r.json()['status'] == pass_data['expect']['status']
    assert r.json()['code'] == pass_data['expect']['code']
    assert r.json()['msg'] == pass_data['expect']['msg']

    # 检查用户在系统中注册成功
    # 1、登录是否成功；2、数据库中查找用户；3、list接口返回值查询是否有改用户

    # 断言注册 方法2：list接口返回值查询是否有改用户

    q = Member.list(baserequest, url)
    assert pass_data['data']['mobilephone'] in q.text

'''
    # 断言注册方法3：登录是否成功
    w = Member.login(baserequest, url,login_data['data'])
    assert login_pass_data['expect']['msg'] in w.text
'''



    # 4、清理环境:删除用户（）
    #MysqlOP.delete_user(db_info, pass_data['data']['mobilephone'])



# 自动化测试原则1：测试环境，在执行脚本前是什么状态，执行完脚本要恢复到之前状态
# 自动化测试原则2：脚本执行依赖的环境，要在脚本中自己构造。比如审核项目，需添调用调价项目的接口准备测试环境
# 自动化测试原则3：脚本之间不能有依赖关系，脚本积累多了，依赖关系混乱，记忆不清
'''
重复注册测试逻辑
环境准备：下发注册请求
测试步骤：下发注册请求（检查结果，报错重复注册
环境恢复：删除用户
pass
'''
