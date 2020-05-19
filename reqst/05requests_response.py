# 导包
import requests
# 发送访问百度首页的接口请求
response = requests.get(url="http://www.baidu.com/")
# 打印响应状态码
print("打印响应状态码{}".format(response.status_code) )
# 打印url
print("打印url：%s" % response.url)
# 打印cookies
print("Cookie为：", response.cookies)
# 打印响应头
print("打印响应头", response.headers)
# 打印编码
print("编码:", response.encoding)
# 打印文本格式的响应体
print("文本格式的响应体", response.text)
# 打印字节码形式的响应体
print("字节码形式的响应体", response.content)
