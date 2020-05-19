# 创建封装的API接口类
class LoginApi:

    # 在实例化类时，要执行的函数
    def __init__(self):
        # 验证码URL
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        # 登录URL
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

    # 封装获取验证码的接口
    def get_verify(self, session):
        """
        :param session: 从外部传入的session会话
        :return: 返回一个Response对象
        """
        return session.get(self.verify_url)

    def login(self, session, data):
        """
        :param session: 从外部传入的session会话
        :param data: 从外部传入的登录请求体数据
        :return: 返回一个包含登录结果Response对象
        """
        return session.post(self.login_url, data=data)


# if __name__ == '__main__':的作用是为了防止导入这个模块时，执行main的函数中的代码
if __name__ == '__main__':
    # 测试封装的接口是否能够使用
    # 1 实例化封装的接口类
    login_api = LoginApi()
    # 2 发送获取验证码请求
    import requests

    session = requests.Session()  # 实例化Session
    response = login_api.get_verify(session)
    print(response.content)  # 输出验证码的获取结果
    # 定义登录的数据
    data = {"username": "13800000002", "password": "123456", "verify_code": "8888"}
    response = login_api.login(session, data)
    print(response.json())  # 输出登录的结果
    session.close()  # 关闭Session
