class Login:
    def __init__(self):
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"

    def get_verify(self, session):
        return session.get(self.verify_url)

    def login(self, session, data):
        return session.post(self.login_url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})