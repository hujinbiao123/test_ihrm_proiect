import time
import unittest

from BeautifulReport import BeautifulReport

from kj_unittest.test_tpshop_login import TestTpshopLogin

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestTpshopLogin))
file_name = "接口测试报告{}.html".format(time.strftime("%Y-%m-%d"))
BeautifulReport(suite).report(filename=file_name, description="接口连接数据库", log_path="./report")
