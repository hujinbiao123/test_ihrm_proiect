# os.path.dirname(os.path.abspath(__file__))
import os

print("__file__:", __file__)
print("os.path.abspath(__file__):", os.path.abspath(__file__))
print("os.path.dirname(os.path.abspath(__file__)):",os.path.dirname(os.path.abspath(__file__)))

# __file__ 定位到执行文件的绝对路径
# os.path.abspath(__file__) 格式化绝对路径，让大部分操作都能使用
# os.path.dirname(os.path.abspath(__file__)) 输出当前执行文件的目录地址
# 简单的理解方式：app.py中的os.path.dirname(os.path.abspath(__file__))，是定位到当前的工程目录