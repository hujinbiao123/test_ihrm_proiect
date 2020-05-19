# 导包
import requests
# 发送查询天气信息的接口请求并获取返回的响应数据
response = requests.get(url="http://www.weather.com.cn/data/sk/101010100.html")
# 使用json格式打印数据
print("JSON格式的数据为：", response.json())
# 使用text格式打印数据
print("TEXT格式的数据为：", response.text)
# 使用字节码形式打印数据
print("字节码形式的数据为：", response.content)

# 由于我们使用json解析数据时，识别的编码格式是ISO-8859-1，所以我们的json格式它采用ISO-8859-1来解析数据
# 所以解析失败
# print("编码格式为：", response.encoding)

# 为了解决编码格式导致的乱码问题，我们有两种方案来解决
# 第一种：手动设置编码
response.encoding = 'utf-8' #手动指定响应体编码格式
# 使用json格式打印数据
print("手动设置编码格式之后，JSON格式的数据为：", response.json())
# 第二种：通过字节码形式数据重新指定编码打印数据
print("过字节码形式数据重新指定编码打印数据结果为：", response.content.decode('utf-8'))