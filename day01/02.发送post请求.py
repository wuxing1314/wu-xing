import requests
import random

# 登录接口;表单格式：content-type：www-x-form-rulenconded，使用data传参

url = 'http://jy001:8081/futureloan/mvc/api/member/login'
cs = {
    'mobilephone':'13812345678',
    'pwd':'123456'
}
r = requests.post(url,data=cs)
print(r.text)
assert r.json()['status']==1

assert "登录成功" in r.text

# 登录接口;json格式：content-ype：application/json，使用json传参
# www.httpbin.org 测试网站，不管什么格式的请求，都封装成json格式的返回
url = "http://www.httpbin.org/post"
cs = {
    'mobilephone':'13812345678',
    'pwd':'123456'
}
r = requests.post(url,data = cs)
print('data传参',r.text)
print('-------------')
r = requests.post(url,json = cs)
print('json传参',r.text)


# 通过接口添加一辆车

url = 'http://127.0.0.1:8080/carRental/car/addCar.action'
cs = {
    "carnumber":"大A88888",
    "cartype":"supercar",
    "color"	:"red",
    "carimg":"images/defaultcarimage.jpg",
    "description":"supercar",
    "price"	:10000000,
    "rentprice":900,
    "deposit":2000,
    "isrenting":random.randint(0,1)
}
head = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}
# Fiddler 抓脚本的包，设置代理
proxy = {
    "http":"http://127.0.0.1:8888", #http协议
    "https": "http://127.0.0.1:8888" #https协议
}
r = requests.post(url,data=cs,headers =head )
print(r.text)