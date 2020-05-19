import requests, unittest

from zy_tpshop.api.api_login import Login
from zy_tpshop.api.api_regist import Regist


class TpshopTpTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 初始化Session实例
        cls.session = requests.Session()
        # 初始化登陆API
        cls.login_api = Login()
        # 初始化注册API
        cls.regist_api = Regist()

    @classmethod
    def tearDownClass(cls):
        if cls.session != None:
            cls.session.close()

    def test01_reg(self):
        # 调用注册的获取验证码接口
        username = 13479289875
        password = 123456
        self.regist_api.get_verify(self.session)
        data = {"auth_code": "TPSHOP", "scene": "1", "username": username, "verify_code": "8888",
                "password": password, "password2": password}

        resposne_reg = self.regist_api.regist(self.session, data=data)
        print(resposne_reg.json())
        self.assertEqual(1, resposne_reg.json().get('status'))
        self.assertEqual("注册成功", resposne_reg.json().get('msg'))
        self.assertEqual(200, resposne_reg.status_code)

    def test02_login(self):
        self.login_api.get_verify(self.session)
        data = {"username": "13800138006", "password": "123456", "verify_code": "8888"}
        response_login = self.login_api.login(self.session, data=data)
        self.assertEqual(1, response_login.json().get('status'))
        self.assertEqual("登陆成功", response_login.json().get('msg'))
        self.assertEqual(200, response_login.status_code)
        print(response_login.json())
