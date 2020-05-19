# 导包
import requests
# 请求IHRM登录接口
# 设置请求头
headers = {"Content-Type":"application/json"}
headers_error = {"Content-Type":"x-www-form-urlencoded"}
response = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                         json={"mobile":"13800000002","password":"123456"},
                         headers=headers)
# 打印结果
print("带上请求头之后的接口登录结果为：", response.json())