'''
pytest 命名约束：
1、文件用test_开头
2、类用Test开头
3、函数或者方法用test_开头
'''
import requests

# 验证密码、注册名输入正确，手机号码值为空，返回码 20103
def test_register_001():
    # 定义接口访问地址，变量
    url = 'http://jy001:8081/futureloan/mvc/api/member/register'
    cs = {
        'mobilephone':'',
        'pwd':123456,
        'regname':'刘老大'
    }
    r = requests.post(url,data=cs)
    assert r.json()['code']=='20103'

# 验证手机号码、注册名输入正确，密码值为空，返回码 20103
def test_register_002():
    # 定义接口访问地址，变量
    url = 'http://jy001:8081/futureloan/mvc/api/member/register'
    cs = {
        'mobilephone':'13112345678',
        'pwd':'',
        'regname':'刘老大'
    }
    r = requests.post(url,data=cs)
    assert r.json()['code']=='20103'

# 验证注册名输入正确，手机号码、密码值为空，返回码 20103
def test_register_003():
    # 定义接口访问地址，变量
    url = 'http://jy001:8081/futureloan/mvc/api/member/register'
    cs = {
        'mobilephone': '',
        'pwd': '',
        'regname': '刘老大'
    }
    r = requests.post(url, data=cs)
    assert r.json()['code'] == '20103'

# 验证密码输入正确，手机号码、注册名值为空，返回码 20103
def test_register_004():
    # 定义接口访问地址，变量
    url = 'http://jy001:8081/futureloan/mvc/api/member/register'
    cs = {
        'mobilephone': '',
        'pwd': '123456',
        'regname': ''
    }
    r = requests.post(url, data=cs)
    assert r.json()['code'] == '20103'

# 验证手机号码输入正确，密码、注册名值为空，返回码 20103
def test_register_005():
    # 定义接口访问地址，变量
    url = 'http://jy001:8081/futureloan/mvc/api/member/register'
    cs = {
        'mobilephone': '13123456789',
        'pwd': '',
        'regname': ''
    }
    r = requests.post(url, data=cs)
    assert r.json()['code'] == '20103'

# 验证手机号码、密码、注册名值为空，返回码 20103
def test_register_006():
    # 定义接口访问地址，变量
    url = 'http://jy001:8081/futureloan/mvc/api/member/register'
    cs = {
        'mobilephone': '',
        'pwd': '',
        'regname': ''
    }
    r = requests.post(url, data=cs)
    assert r.json()['code'] == '20103'

# 验证密码、注册名输入正确，手机号码为空，返回码 20103
def test_register_007():
    # 定义接口访问地址，变量
    url = 'http://jy001:8081/futureloan/mvc/api/member/register'
    cs = {

        'pwd': '',
        'regname': ''
    }
    r = requests.post(url, data=cs)
    assert r.json()['code'] == '20103'

# 验证手机号码、注册名输入正确，密码为空，返回码 20103
def test_register_008():
    # 定义接口访问地址，变量
    url = 'http://jy001:8081/futureloan/mvc/api/member/register'
    cs = {
        'mobilephone': '12356785678',
        'regname': '张老三'
    }
    r = requests.post(url, data=cs)
    assert r.json()['code'] == '20103'

# 验证注册名输入正确，手机号码、密码为空，返回码 20103
def test_register_009():
    # 定义接口访问地址，变量
    url = 'http://jy001:8081/futureloan/mvc/api/member/register'
    cs = {

        'regname': '张老三'
    }
    r = requests.post(url, data=cs)
    assert r.json()['code'] == '20103'

# 验证密码输入正确，手机号码、注册名为空，返回码 20103
def test_register_010():
    # 定义接口访问地址，变量
    url = 'http://jy001:8081/futureloan/mvc/api/member/register'
    cs = {

        'pwd': '123456'
    }
    r = requests.post(url, data=cs)
    assert r.json()['code'] == '20103'

# 验证手机号码输入正确，密码、注册名为空，返回码 20103
def test_register_011():
    # 定义接口访问地址，变量
    url = 'http://jy001:8081/futureloan/mvc/api/member/register'
    cs = {

        'mobilephone': '12356785678'
    }
    r = requests.post(url, data=cs)
    assert r.json()['code'] == '20103'

# 验证手机号码、密码、注册名为空，返回码 20103
def test_register_012():
    # 定义接口访问地址，变量
    url = 'http://jy001:8081/futureloan/mvc/api/member/register'
    cs = {
    }
    r = requests.post(url, data=cs)
    assert r.json()['code'] == '20103'


# 验证手机号码、密码输入正确，注册名入参2次时，注册失败
def test_register_013():
    # 定义接口访问地址，变量
    url = 'http://jy001:8081/futureloan/mvc/api/member/register'
    cs = {
        'mobilephone':'13124563458',
        'pwd':123456,
        'pwd': 123458,
        'regname':'刘老大'
    }
    r = requests.post(url,data=cs)
    assert r.json()['code']=='20110'
