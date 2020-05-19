# 导包
import pymysql
# 建立连接:注意在pymysql操作数据库时，插入语句可以把事务开关开启，这样才能提交事务
# autocommit=True
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       database='books',
                       charset='utf8',
                       autocommit=True)
# 获取游标
cursor = conn.cursor()
# 执行SQL：插入一本图书到t_book表
insert_sql = "insert into t_book(`id`, `title`, `pub_date`) VALUES(4, '西游记', '1986-01-01');"
# 执行
cursor.execute(insert_sql)
# 关闭游标
cursor.close()
# 关闭连接
conn.close()