'''
requests.session  保持状态，自动管理过程中产生的cookie，
下次请求自动带着上次请求的cookie
'''

import requests
from requests import utils

s = requests.session()
print(s.cookies)
print("登录前cookie：",utils.dict_from_cookiejar(s.cookies))

# 登录接口
url = 'https://www.bagevent.com/user/login'
cs = {
'access_type':	'1',
'loginType':	'1',
'emailLoginWay':'0',
'account':	'2780487875@qq.com',
'password':	'qq2780487875',
'remindmeBox':	'on',
'remindme':'1'
}
r = s.post(url,data=cs)
print(s.cookies)
print("登录后cookie：",utils.dict_from_cookiejar(s.cookies))

#dashboard接口
url = 'https://www.bagevent.com/account/dashboard'
r = s.get(url)
# print(r.text)
assert '<meta name="company" content="南京弟齐信息技术有限公司"/>' in r.text
print(s.cookies)
