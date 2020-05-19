# 导包
import pymysql

# 建立连接
conn = pymysql.connect(host='localhost', user='root', password='root', database='books')
# 获取游标
cursor = conn.cursor()
# 执行SQL语句
sql = "select version()"
cursor.execute(sql)
# 打印执行结果
result = cursor.fetchone()
print("结果result为：", result)
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
