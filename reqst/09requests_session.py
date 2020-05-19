# 导包
import requests

# 创建session实例
session = requests.Session()
# 定义验证码、登录、我的订单页面的URL
verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
order_url = "http://localhost/Home/Order/order_list.html"
# 使用session实例发送获取验证码接口请求：服务器会把验证码和令牌都返回，并保存到session中
response_verify = session.get(url=verify_url)
# 使用session实例发送登录接口请求：使用session发送请求时，session会自动把cookies发送给服务器
response_login = session.post(url=login_url,
                              data={"username": "13800138006", "password": "123456", "verify_code": "8888"})
# 使用session实例发送我的订单页面接口请求
response_order = session.get(url=order_url)

# 打印结果
print("登录结果为：", response_login.json())
# 关闭
session.close()