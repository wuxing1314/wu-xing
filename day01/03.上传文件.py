import requests

url = 'http://127.0.0.1:8080/carRental/file/uploadFile.action'
#本地存放的文件
file = 'd:/xiaoxin.jpg'
# 打开文件
with open(file,mode='rb') as f:
    #{'name':file-tiple}
    # file-tiple:('filename',fileobj,'content_type')
    cs = {'mf':(file,f,'image/jpg')}
    r = requests.post(url,files = cs)
    print(r.text)
    uploadPath = r.json()['data']['src']



url = 'http://127.0.0.1:8080/carRental/car/addCar.action'
cs = {
    "carnumber":"删A88888",
    "cartype":"supercar",
    "color"	:"red",
    "carimg":uploadPath,
    "description":"supercar",
    "price"	:10000000,
    "rentprice":900,
    "deposit":2000,
    "isrenting":0
}
head = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}
q = requests.post(url,data=cs,headers = head)
print(q.text)


