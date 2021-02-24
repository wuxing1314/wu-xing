'''
1、get、post方法做异常处理
2、打印日志
3、保持会话，使用session发送请求
'''
import requests


class BaseRequests:
    def __init__(self):
        self.session = requests.session()

    # 重写get
    def get(self, url, **Kwargs):
        try:
            r = self.session.get(url, **Kwargs)
            return r
        except Exception as e:
            print(f"发送get请求,url:{url},请求参数：{Kwargs}，异常信息为{e}")

    # 重写post
    def post(self, url, **Kwargs):
        try:
            r = self.session.post(url, **Kwargs)
            return r
        except Exception as e:
            print(f"发送post请求,url:{url},请求参数：{Kwargs}，异常信息为{e}")


if __name__ == '__main__':
    r = BaseRequests().get("http://192.168.1.64:8089/futureloan/mvc/api/memberwithdraw")
    print(r.text)
    q = BaseRequests().post("http://192.168.1.64:8089/futureloan/mvc/api/member/login", data={"mobilephone":18012345678,"pwd":123456})
    print(q.text)
