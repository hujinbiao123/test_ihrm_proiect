# 导包
import requests
import unittest
from tp_shop.api.login import LoginApi


# 创建测试类并集成unittest.TestCase


class TestTpshopLogin(unittest.TestCase):

    # 把Unittest常见的初始化函数都写好
    def setUp(self):
        # 1 实例化Session
        self.session = requests.Session()
        # 实例化封装的接口
        self.login_api = LoginApi()

    def tearDown(self):
        # 关闭Session
        if self.session != None:
            self.session.close()

    # 编写测试用例脚本
    def test01_login_success(self):
        # 2 使用在setUp中实例化的封装的接口来发送获取验证码接口请求
        response_verify = self.login_api.get_verify(self.session)
        # 3 按照用例的描述，断言验证码是不是一个图片
        self.assertIn("image", response_verify.headers.get("Content-Type"))
        # 4 使用setUp实例化的封装接口变量发送登录请求
        data = {"username": "13800138006", "password": "123456", "verify_code": "8888"}
        response_login = self.login_api.login(self.session, data=data)
        print("登录的结果为：", response_login.json())
        # 5 按照用户的描述，断言登录的结果
        self.assertEqual(200, response_login.status_code)  # 断言响应状态码
        self.assertEqual(1, response_login.json().get("status"))
        self.assertIn("登陆成功", response_login.json().get("msg"))

    def test02_username_is_not_exist(self):
        # 2 使用在setUp中实例化的封装的接口来发送获取验证码接口请求
        response_verify = self.login_api.get_verify(self.session)
        # 3 按照用例的描述，断言验证码是不是一个图片
        self.assertIn("image", response_verify.headers.get("Content-Type"))
        # 4 使用setUp实例化的封装接口变量发送登录请求
        data = {"username": "13900138006", "password": "123456", "verify_code": "8888"}
        response_login = self.login_api.login(self.session, data=data)
        print("登录的结果为：", response_login.json())
        # 5 按照用户的描述，断言登录的结果
        self.assertEqual(200, response_login.status_code)  # 断言响应状态码
        self.assertEqual(-1, response_login.json().get("status"))
        self.assertIn("账号不存在", response_login.json().get("msg"))

    def test03_password_is_error(self):
        # 2 使用在setUp中实例化的封装的接口来发送获取验证码接口请求
        response_verify = self.login_api.get_verify(self.session)
        # 3 按照用例的描述，断言验证码是不是一个图片
        self.assertIn("image", response_verify.headers.get("Content-Type"))
        # 4 使用setUp实例化的封装接口变量发送登录请求
        data = {"username": "13800138006", "password": "error", "verify_code": "8888"}
        response_login = self.login_api.login(self.session, data=data)
        print("登录的结果为：", response_login.json())
        # 5 按照用户的描述，断言登录的结果
        self.assertEqual(200, response_login.status_code)  # 断言响应状态码
        self.assertEqual(-2, response_login.json().get("status"))
        self.assertIn("密码错误", response_login.json().get("msg"))
