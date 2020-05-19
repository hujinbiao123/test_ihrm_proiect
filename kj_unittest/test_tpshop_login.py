# 写代码时，不应该先记住应该导入什么模块（包）。而是应该熟练应该写什么代码，这些代码依赖了哪些包
# 核心模块都要记住：掌握导入unittest和requests

# 导包
import requests
import unittest


# 创建支持unittest框架的类
class TestTpshopLogin(unittest.TestCase):

    # setUp函数是unittest框架中的函数，只有集成unittest框架之后，这个函数才会发挥它该有的作用
    # 作用：每次执行unittest框架中的测试用例时，都会先运行setUp函数中的代码
    def setUp(self):
        # 在setUp中实例化Session
        self.session = requests.Session()
        # 验证码URL
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        # 登录URL
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

    # tearDown的作用
    # 每次执行完每个unittest框架的测试用例后,都会运行tearDown中的代码
    def tearDown(self):
        # 在tearDown中关闭Session
        if self.session != None:
            self.session.close()

    # 编写测试登录成功的代码
    # test是unittest框架中默认识别测试用例的前缀标识符
    # test01后面的01数字，是指按照序号01来执行用例，01代表第一个执行，如果不写，那么随机执行
    def test01_login_success(self):
        # 使用session发送获取验证码的接口请求
        response_verify = self.session.get(url=self.verify_url)
        # 断言验证码是不是一个图片
        # 打印出响应头
        response_headers = response_verify.headers
        print("获取到的响应头为：", response_headers)
        # 进行实际的断言
        self.assertIn("image/png", response_headers.get("Content-Type"))

        # 发送登录请求
        data = {"username": "13800138006", "password": "123456", "verify_code": "8888"}
        response_login = self.session.post(url=self.login_url, data=data)
        # 打印登录的响应数据
        print("登录的响应数据为：", response_login.json())
        # 断言登录的数据
        self.assertEqual(200, response_login.status_code)  # 断言响应状态码
        self.assertEqual(1, response_login.json().get("status"))  # 断言status的值
        self.assertIn("登陆成功", response_login.json().get("msg"))  # 断言message的值

    def test02_username_is_not_exist(self):
        # 使用session发送获取验证码的接口请求
        response_verify = self.session.get(url=self.verify_url)
        # 断言验证码是不是一个图片
        # 打印出响应头
        response_headers = response_verify.headers
        print("获取到的响应头为：", response_headers)
        # 进行实际的断言
        self.assertIn("image/png", response_headers.get("Content-Type"))

        # 发送登录请求
        data = {"username": "13900138006", "password": "123456", "verify_code": "8888"}
        response_login = self.session.post(url=self.login_url, data=data)
        # 打印登录的响应数据
        print("登录的响应数据为：", response_login.json())
        # 断言登录的数据
        self.assertEqual(200, response_login.status_code)  # 断言响应状态码
        self.assertEqual(-1, response_login.json().get("status"))  # 断言status的值
        self.assertIn("账号不存在", response_login.json().get("msg"))  # 断言message的值

    def test03_password_is_error(self):
        # 使用session发送获取验证码的接口请求
        response_verify = self.session.get(url=self.verify_url)
        # 断言验证码是不是一个图片
        # 打印出响应头
        response_headers = response_verify.headers
        print("获取到的响应头为：", response_headers)
        # 进行实际的断言
        self.assertIn("image/png", response_headers.get("Content-Type"))

        # 发送登录请求
        data = {"username": "13800138006", "password": "1234567", "verify_code": "8888"}
        response_login = self.session.post(url=self.login_url, data=data)
        # 打印登录的响应数据
        print("登录的响应数据为：", response_login.json())
        # 断言登录的数据
        self.assertEqual(200, response_login.status_code)  # 断言响应状态码
        self.assertEqual(-2, response_login.json().get("status"))  # 断言status的值
        self.assertIn("密码错误", response_login.json().get("msg"))  # 断言message的值
