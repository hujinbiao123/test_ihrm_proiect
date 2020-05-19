# 导包
import pymysql

# 建立连接
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       database='books',
                       autocommit=True)
# 获取游标
cursor = conn.cursor()
# 执行sql
insert_book = "insert into t_comment(book_id,name,content,create_time) values(1,'猪猪侠', '童年的回忆', '2020-01-01 20:01:01');"
cursor.execute(insert_book)
update_book = "update t_book set comment=comment+1 where id=1"
cursor.execute(update_book)
print(cursor.fetchall())
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
