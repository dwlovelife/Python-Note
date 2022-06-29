import urllib.request
import urllib.parse

# GET 请求
response = urllib.request.urlopen("http://wwww.baidu.com")
print(response.read().decode("utf-8"))

# POST请求
data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
response = urllib.request.urlopen("http://httpbin.org/get")
print(response.read().decode("utf-8"))

# 超时处理
try:
    response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.1)
    print(response.read().decode("utf-8"))
except urllib.error.URLError as e:
    print("time out")

#获取响应状态
response = urllib.request.urlopen("http://www.baidu.com")
print(response.status)

url = "https://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))