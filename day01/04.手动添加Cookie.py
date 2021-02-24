'''
Cookie 识别用户
'''

import requests

# 没有登录时，返回跳转登录页面
url = 'https://www.bagevent.com/account/dashboard'
r = requests.get(url)
print(r.text)
print('----------------------------------------------------------')
# 发送请求时，带上cookie信息，在header里边
head = {
'Cookie': '_ga=GA1.2.1547377711.1611729450; _gid=GA1.2.1380777121.1611729450; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1611729450; __auc=01617961177428fbae464d92788; MEIQIA_TRACK_ID=1ndr61sETZ3of88QtTM1LSZS1j6; __asc=59f064a117747db77b4a19d3064; MEIQIA_VISIT_ID=1ngn0Nf9SHCe7r8poKaBeRsxWlS; BAGSESSIONID=e17a4caa-aaae-4afb-ae9b-2ba969674ab7; JSESSIONID=208561F616E149DC05226DCA9599C4C7; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1611820464; _gat=1; BAG_EVENT_TOKEN_=02de735f68204d51009e7edda78e58c13a3fcdd1; BAG_EVENT_CK_KEY_="2780487875@qq.com"; BAG_EVENT_CK_TOKEN_=2440f5d17af838308ba4b390db81af38'}

r = requests.get(url,headers =head)
print(r.text)

'''
缺点：
1、cookie会失效，失效后需重新获取
2、登陆后的每个接口，需要重新带着cookie
'''