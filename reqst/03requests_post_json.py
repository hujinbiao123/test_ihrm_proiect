# 导包
import requests

# 发送post请求，提交json数据（ihrm登录接口）和接收返回的响应数据
response = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                         json={"mobile": "13800000002", "password": "123456"})
# 打印响应数据
print("ihrm登录接口返回的结果为：", response.json())
