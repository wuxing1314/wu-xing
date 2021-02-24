'''
Mock:1、接口测试的时候，场景比较难模拟，不好构造。用Mock模拟某个接口的返回值
     2、依赖其他项目的接口，但是该接口尚未开发完成，自己所在项目的接口已经开发完成，没有依赖接口的环境，如何测试
'''
from unittest import mock

import requests

#接口地址：http://www.zhifu.com/pay
#方法：post
#参数：{'订单':123,'支付金额':123,'支付方式':'余额宝'}
#返回值：{‘code’：100001，'msg':'支付成功'}
#返回值：{‘code’：100001，'msg':'支付失败'}
def zhifu(data):
    r = requests.post('http://www.zhifu.com/pay',data)
    return r.json()

def test_zhifu():
    data = {'订单':123,'支付金额':123,'支付方式':'余额宝'}
    #　return_value是Mock里的参数
    zhifu = mock.Mock(return_value={'code':100001,'msg':'支付成功'})
    r=zhifu(data)
    print(r)

def withdraw(data):
    r = requests.post('http://jy001:8081/futureloan/mvc/api/member/withdraw', data)
    return r.json()

@mock.patch('test_012.zhifu',return_value={'code':100001,'msg':'支付成功'})
def test_zhifu2(a):  # 方法里边不许传一个参数，但在方法内没有用到
    data = {'订单':123,'支付金额':123,'支付方式':'余额宝'}
    r = zhifu(data)
    assert r['msg'] == '支付成功'

#练习：金融项目，注册用户--> 登录--> 充值1000--> 取现100 （服务器异常）
def test_register():
    r = requests.post('http://jy001:8081/futureloan/mvc/api/member/register',
                  {'mobilephone':'15112346789','pwd':'123456'})
    assert r.json()['code']=='20110'

def test_login():
    r=requests.post('http://jy001:8081/futureloan/mvc/api/member/login',
                  {'mobilephone': '15112346789', 'pwd': '123456'})
    assert r.json()['code'] == '10001'

def test_recharge():
    r=requests.post('http://jy001:8081/futureloan/mvc/api/member/recharge',
                  {'mobilephone': '15112346789', 'amount': '1000'})
    assert r.json()['code'] == '10001'

@mock.patch('test_012.withdraw',return_value={'status': 0, 'code': '20102', 'data': None, 'msg': '取现成功'})
def test_withdraw(a):
    r = withdraw({'mobilephone': '15112346789', 'amount': '100'})
    assert r['msg'] == '取现成功'
