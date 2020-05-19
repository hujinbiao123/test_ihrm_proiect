# 1 我们先用设计模式实现ihrm登录
# 2 根据我们设计模式的实现封装ihrm登录接口
# 3 根据封装的接口，优化ihrm登录的代码
# 导包
import unittest
import logging
import requests
# 导入封装的API
from parameterized import parameterized

from test_ihrm_project import app
from test_ihrm_project.api.login_api import TestLoginApi

# 创建测试类，继承unittest.TestCase模块
from test_ihrm_project.utils import read_login_data, assert_common


class TestIHRMLogin(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"

        self.login_api = TestLoginApi()  # 实例化登录API

    def tearDown(self):
        ...

    filename = app.BASE_DIR + "/data/login_data.json"

    @parameterized.expand(read_login_data(filename))
    # 编写第一个案例，测试登录成功
    def test01_login(abc, case_name, jsonData, http_code, success, code, message):
        # IHRM项目可以直接发送登录请求
        headers = {"Content-Type": "application/json"}  # 定义请求头
        jsonData = jsonData
        # 发送登录请求
        response = abc.login_api.login(jsonData, headers)
        # 打印登录的结果cvf
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 使用封装的通用断言函数实现优化断言
        assert_common(http_code, success, code, message, response, abc, )
