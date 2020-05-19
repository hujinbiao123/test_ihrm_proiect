class Regist:
    def __init__(self):
        self.regist_url = "http://localhost/index.php/Home/User/reg.html"
        self.verify_url = "http://localhost/index.php/Home/User/verify/type/user_reg.html"

    def get_verify(self, session):
        return session.get(self.verify_url)

    def regist(self, session, data):
        return session.post(self.regist_url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})
