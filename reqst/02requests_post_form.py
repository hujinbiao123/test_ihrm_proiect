# 导包
import requests

# 发送post请求完成tpshop登录接口的调用（提交表单数据）和接收响应结果
response = requests.post(url="http://localhost/index.php?m=Home&c=User&a=do_login",
                         data={"username": "13800138006", "password": "123456", "verify_code": "8888"})
# 打印响应结果
print(response.text)
# 用json格式展示数据
print(response.json())
