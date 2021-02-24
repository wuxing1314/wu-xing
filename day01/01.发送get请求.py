'''
接口测试：
    使用request中的get和post方法调用接口，检查返回值是否正确
'''

import requests
'''
get请求，不带参数

url = 'http://jy001:8081/futureloan/mvc/api/member/list'
#发送get请求
r = requests.get(url)
#打印响应
print(r.text)
#检查结果是否与与其相同
assert r.status_code == 200
assert r.reason =="OK"

rjson = r.json()
assert rjson['status'] ==1
assert rjson['code'] == '10001'
assert rjson['msg'] == "获取用户列表成功"
print(r.headers)
'''

'''
get带参数


url = 'http://jy001:8081/futureloan/mvc/api/member/register'
# 发送get请求
r = requests.get(url)
# 打印响应
print(r.text)
rjson = r.json()
assert rjson["status"]==1
assert rjson['code']=='10001'
'''

'''
#注册接口，使用param传参
url = 'http://jy001:8081/futureloan/mvc/api/member/register'
cs = {
    "mobilephone":"13812345678",
    "pwd":"123456",
    "regname":"二狗子"
}

# 发送get请求
r = requests.get(url,params=cs)
# 打印响应
print(r.text)
rjson = r.json()
assert rjson["status"]==0
assert rjson['code']=='20110'
assert rjson['msg'] == "手机号码已被注册"
'''

'''
查询手机号码接口
'''
url = 'https://tcc.taobao.com/cc/json/mobile_tel_segment.htm'
cs = {
    'tel':'18392569119'
}
r = requests.get(url,params=cs)
print(r.text)

assert '陕西' in r.text

