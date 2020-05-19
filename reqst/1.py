# 导包
import requests

# 获取返回的令牌
response = requests.post("http://ihrm-test.itheima.net/api/sys/login",
                         json={"mobile": "13800000002", "password": "123456"},
                         headers={"Content-Type": "application/json"})

print(response.url)
print(response.encoding)
print(response.cookies)
print(response.headers)
print(response.json())
token = response.json().get("data")
response = requests.post("http://ihrm-test.itheima.net/api/sys/profile", headers
={"Content-Type": "application/json", "Authorization": token})
print(response.json())
