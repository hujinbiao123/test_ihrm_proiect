# 导包
import requests
# 发送访问百度搜索接口的请求
# 直接在url中传递查询参数
# response = requests.get(url="http://www.baidu.com/S?wd=翻身鱼") # 直接在url中传递查询参数
# # 打印结果
# print("百度搜索的结果为：", response.text)

# 通过params参数编写字典格式的查询参数进行搜索
# response = requests.get(url="http://www.baidu.com/S", params={"wd":"名侦探柯南"})
# # 打印结果
# print("通过params参数编写字典格式的查询参数进行搜索结果为：", response.text)

# 通过params参数编写url形式的查询参数进行搜索
response = requests.get(url="http://www.baidu.com/S", params="wd=架构师")
# 打印结果
print("通过params参数编写url形式的查询参数进行搜索", response.text)