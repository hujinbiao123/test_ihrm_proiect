# 1 我们先用设计模式实现ihrm登录
# 2 根据我们设计模式的实现封装ihrm登录接口
# 3 根据封装的接口，优化ihrm登录的代码
# 导包
import unittest
import logging
import requests
# 导入封装的API
from test_ihrm_project.api.login_api import TestLoginApi


# 创建测试类，继承unittest.TestCase模块
from test_ihrm_project.utils import assert_common


class TestIHRMLogin(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"

        self.login_api = TestLoginApi()  # 实例化登录API

    def tearDown(self):
        ...

    # 编写第一个案例，测试登录成功
    def test01_login_success(abc):
        # IHRM项目可以直接发送登录请求
        headers = {"Content-Type": "application/json"}  # 定义请求头
        jsonData = {"mobile": "13800000002", "password": "123456"}
        # 发送登录请求
        response = abc.login_api.login(jsonData, headers)
        # 打印登录的结果cvf
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # # 断言登录的结果
        # self.assertEqual(200, response.status_code)  # 断言响应状态码
        # self.assertEqual(True, result.get("success"))  # 断言success
        # self.assertEqual(10000, result.get("code"))  # 断言code
        # self.assertIn("操作成功", result.get("message"))  # 断言message

        # 使用封装的通用断言函数实现优化断言
        assert_common(200, True, 10000, "操作成功", response, abc)

    def test02_mobile_is_not_exist(self):
        # 定义请求头
        headers = {"Content-Type": "application/json"}
        jsonData = {"mobile": "13900000002", "password": "123456"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 断言
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test03_password_is_error(self):
        # 定义请求头
        headers = {"Content-Type": "application/json"}
        jsonData = {"mobile": "13800000002", "password": "error"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 断言
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test04_mobile_is_empty(self):
        # 定义请求头
        headers = {"Content-Type": "application/json"}
        jsonData = {"mobile": "", "password": "error"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 断言
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test05_password_is_empty(self):
        # 定义请求头
        headers = {"Content-Type": "application/json"}
        jsonData = {"mobile": "13800000002", "password": ""}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 断言
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test06_mobile_has_special_char(self):
        # 定义请求头
        headers = {"Content-Type": "application/json"}
        jsonData = {"mobile": "138(0000002", "password": "123456"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 断言
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test07_more_params(self):
        # 定义请求头
        headers = {"Content-Type": "application/json"}
        jsonData = {"mobile": "13800000002", "password": "123456", "more_params": "1"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 断言
        assert_common(200, True, 10000, "操作成功", response, self)

    def test08_less_mobile(self):
        # 定义请求头
        headers = {"Content-Type": "application/json"}
        jsonData = {"password": "123456"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 断言
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test09_less_password(self):
        # 定义请求头
        headers = {"Content-Type": "application/json"}
        jsonData = {"mobile": "13800000002"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 断言
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test10_none_params(self):
        # 定义请求头
        headers = {"Content-Type": "application/json"}
        jsonData = {}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 断言
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test11_error_params(self):
        # 定义请求头
        headers = {"Content-Type": "application/json"}
        jsonData = {"mboile": "13800000002", "password": "123456"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 断言
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test12_None(self):
        # 定义请求头
        headers = {"Content-Type": "application/json"}
        jsonData = None
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 断言
        assert_common(200, False, 99999, "抱歉，系统繁忙，请稍后重试！", response, self)
