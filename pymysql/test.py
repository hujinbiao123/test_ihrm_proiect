import pymysql

conn = pymysql.connect(host="localhost", user="root", password="root", database="books", autocommit=True,
                       charset='utf8')
cursor = conn.cursor()

sql = "insert into t_book(title,pub_date) values('西游记2', '1986-01-01')"
cursor.execute(sql)

cursor.close()
conn.close()