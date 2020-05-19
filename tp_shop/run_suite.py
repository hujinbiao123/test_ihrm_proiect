import time
import unittest
from BeautifulReport import BeautifulReport

from test_ihrm_project.script.test_ihrm_login import TestIHRMLogin

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestIHRMLogin))
file_name = "ihrm接口测试报告{}.html".format(time.strftime("%Y-%m-%d"))
BeautifulReport(suite).report(filename=file_name, description="test_ihrm", log_path="./report")
