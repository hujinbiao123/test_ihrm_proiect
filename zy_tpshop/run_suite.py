import time
import unittest

from BeautifulReport import BeautifulReport

from zy_tpshop.report.test_tpshop_login import TpshopTpTest

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TpshopTpTest))
file_name = "pshop接口测试报告{}.html".format(time.strftime("%Y-%m-%d"))
BeautifulReport(suite).report(filename=file_name, description="接口连接数据库", log_path="./report")
