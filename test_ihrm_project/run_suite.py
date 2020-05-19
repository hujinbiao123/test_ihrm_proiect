import time
import unittest

from BeautifulReport import BeautifulReport

from test_ihrm_project.script.test_ihrm_emp_params import TestIHRMEmployee3
from test_ihrm_project.script.test_ihrm_login_params import TestIHRMLogin

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestIHRMEmployee3))
suite.addTest(unittest.makeSuite(TestIHRMLogin))
file_name = "ihrm员工接口测试报告{}.html".format(time.strftime("%Y-%m-%d"))
BeautifulReport(suite).report(filename=file_name, description="接口连接数据库", log_path="./report")
