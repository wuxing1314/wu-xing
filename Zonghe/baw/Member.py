'''
金融项目用户管理模块的接口
例：http://192.168.1.64:8089/futureloan/mvc/api/member/list
member是模块名
List是接口名
'''

def register(baserequest,url,data):
    '''

    :param baserequests:
    :param url:
    :param data:
    :return:
    '''
    url = url+"futureloan/mvc/api/member/register"
    r = baserequest.post(url,data=data)
    return r


def list(baserequest,url):
    url = url + "futureloan/mvc/api/member/list"
    r = baserequest.get(url)
    return r


def login(baserequest,url,data):
    url = url + "futureloan/mvc/api/member/login"
    r = baserequest.post(url,data=data)
    return r

def recharge(baserequest,url,data):
    url = url + "futureloan/mvc/api/member/recharge"
    r = baserequest.post(url,data=data)
    return r

