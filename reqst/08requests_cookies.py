# 导包
import requests

# 发送获取验证码的请求
response_verify = requests.get(url="http://localhost/index.php?m=Home&c=User&a=verify")
# 提取服务器返回的cookies（cookies中有令牌）
cookies = response_verify.cookies
# 发送登录接口请求（带上cookies），完成登录成功的请求
response_login = requests.post(url="http://localhost/index.php?m=Home&c=User&a=do_login",
                               data={"username": "13800138006", "password": "123456", "verify_code": "8888"},
                               cookies=cookies)
print("加上cookies的运行结果为：", response_login.json())
# 请求我的订单页面
response_order = requests.get(url="http://localhost/Home/Order/order_list.html",
                              cookies=cookies)
print("订单页面的结果为：", response_order.text)
