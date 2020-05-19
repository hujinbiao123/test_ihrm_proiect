# 导包
import pymysql
# 建立连接
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       database='books',
                       autocommit=True,
                       charset='utf8')
# 获取游标
cursor = conn.cursor()
# 执行删除语句
delete_sql = "DELETE FROM T_BOOK WHERE `TITLE` = '西游记';"
# 执行
cursor.execute(delete_sql)
# 关闭游标
cursor.close()
# 关闭连接
conn.close()