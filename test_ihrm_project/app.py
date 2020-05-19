import logging
import os
from logging import handlers

# 定义全局变量headers，提供给script中导入使用
HEADERS = None
# 定义全局变量EMPID，提供给添加、查询、修改、删除员工使用
EMPID = None
BASE_DIR = filename = os.path.dirname(os.path.abspath(__file__))


# os.path.dirname(os.path.abspath(__file__)) 作用是自动根据当前执行的py文件
# 找到这个python文件目录：简单的说，在我们这个项目里面，帮助定位到项目工程目录

# 1 创建一个初始化日志的函数
def init_logging():
    # 2 在函数中创建日志器
    logger = logging.getLogger()
    # 3 设置日志等级
    logger.setLevel(logging.INFO)
    # 4 创建处理器
    # 控制台处理器：将日志输出到控制台
    sh = logging.StreamHandler()
    # 文件处理器：将日志输出到文件当中:
    fh = logging.handlers.TimedRotatingFileHandler(
        filename=BASE_DIR + "/log/ihrm.log", when='S', interval=5, backupCount=3, encoding='utf-8')
    # 5 创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 6 将格式化器添加到处理器当中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 7 将处理器添加到日志器当中
    logger.addHandler(sh)
    logger.addHandler(fh)
    # 8 在api模块下的__init__.py文件中进行初始化
