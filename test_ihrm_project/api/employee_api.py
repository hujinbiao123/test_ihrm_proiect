# 导包
import requests
# 创建员工的api类
class TestEmployeeApi:
    def __init__(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"
        self.emp_url = "http://ihrm-test.itheima.net" + "/api/sys/user"

    # 封装添加员工的函数
    def add_emp(self,headers, username, mobile):
        # 添加员工
        response = requests.post(self.emp_url,
                                 json={
                                     "username": username,
                                     "mobile": mobile,
                                     "timeOfEntry": "2020-05-05",
                                     "formOfEmployment": 1,
                                     "workNumber": "1234123",
                                     "departmentName": "测试部",
                                     "departmentId": "1063678149528784896",
                                     "correctionTime": "2020-05-17T16:00:00.000Z"
                                 },
                                 headers=headers)
        return response

    def query_emp(self, emp_id, headers):
        # 定义查询员工的url
        query_url = self.emp_url + "/" + emp_id
        # 发送查询员工请求
        response = requests.get(query_url, headers=headers)
        return response

    def modify_emp(self, emp_id, headers, username):
        # 定义修改员工的url
        modify_url = self.emp_url + "/" + emp_id
        # 发送修改员工请求
        response = requests.put(url=modify_url,
                                json={"username":username},
                                headers=headers)
        return response

    def delete_emp(self, emp_id, headers):
        # 定义删除员工的URL
        delete_url = self.emp_url + "/" + emp_id
        # 发送删除员工的请求
        response = requests.delete(url=delete_url, headers=headers)
        return response