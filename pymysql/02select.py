#! encoding='utf-8'
# 导包
import pymysql

# 建立连接
conn = pymysql.connect(host='localhost', user='root', password='root', database='books', charset='utf8')
# 获取游标
cursor = conn.cursor()
# 执行SQL语句
# 需求：执行查询图书表的数据，要显示图书的ID,图书名称，阅读量，评论量
sql = "select `id`,`title`,`read`,`comment` from t_book;"
# 执行
cursor.execute(sql)
# 执行之后，要查询结果的记录数目:cursor.rowcount 会返回结果的记录数目
print("结果的记录数目:", cursor.rowcount)
# 打印第一条数据:cursor.fetchone() 打印第一条数据，在代码中，如果执行多次，会每次打印下一行数据，直接数据为空
print("第一条数据：", cursor.fetchone())
# 打印全部数据：cursor.fetchall() 打印全部数据
# 由于fetchone执行后，指向数据的指针下移导致fetchall不会返回所有的数据，所以我们需要重置指针
# 重置方法：重新执行查询语句
cursor.execute(sql)
# 获取全部数据
all_books = cursor.fetchall()
print("全部数据为：", all_books)
# 打印每一本书
for book in all_books:
    print(book[1])
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
