# 导包
import pymysql
# 建立连接 : 注意 由于我们需要手动演示提交事务，所以自动提交事务的开关不要打开
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       database='books',
                       charset='utf8')
# 获取游标
cursor = conn.cursor()
# 执行：插入一本书和插入一个英雄人物
insert_book = "insert into t_book(`title`,`pub_date`,`read`) VALUES('三体:黑暗森林','1989-01-01','1000000');"
insert_hero = "insert into t_hero(`name`,`gender`,`description`,`book_id`) VALUES('逻辑',1,'是一个伟大的人',5);"
# 执行两个SQL语句
cursor.execute(insert_book)
cursor.execute(insert_hero)
# 执行之后，由于没有提交事务，所以我们插入的一本书和英雄人物都没有进入数据库，在navicat中无法查看
# 我们可以在代码中查询，看代码事务当中，是否有插入的书
# 执行查询图书语句
cursor.execute("select * from t_book;")
# 接收执行接口
result = cursor.fetchall()
# 打印执行结果
print("图书：", result)
# 执行查询英雄人物的语句
cursor.execute("select * from t_hero;")
# 获取结果
result = cursor.fetchall()
# 打印结果
print("英雄人物：", result)
# 提交事务的分界线
print("-"* 100)
conn.commit() # 如果不提交事务，那么在数据库当中，会看不出我们插入的数据
# 关闭游标
cursor.close()
# 关闭连接
conn.close()