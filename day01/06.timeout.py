'''
1、上传文件的接口，上传文件大小不同时，耗时不同，默认时间不够用时候，可以设置接口超时时间
2、接口性能测试，看接口是否能在某个时间内返回
'''
import requests

for i in range(10):
    try:
        r = requests.get('http://jy001:8081/futureloan/mvc/api/member/list',timeout=0.05)
        print(r.text)
    except Exception as e:
        print(e)

