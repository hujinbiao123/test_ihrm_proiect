# 编写初始化日志的代码
import logging
# 导入app.py模块
from test_ihrm_project import app

# 调用app.py中初始化日志的函数


app.init_logging()
# 打印日志，调试结果
logging.info("测试日志是否会打印！")
