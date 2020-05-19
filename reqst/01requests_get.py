# 导包
import requests

# 发送Get请求并获取响应数据
response = requests.get(url="http://www.baidu.com/s?wd=猪猪侠")
# response = requests.get(url="http://www.baidu.com/s", params="wd=猪猪侠")
# response = requests.get(url="http://www.baidu.com/s", params={'wd': '猪猪侠'})
# 打印响应数据
print(response.text)
