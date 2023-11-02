import sqlite3
vv=["sdsd","jkj0","jkjk","jjk","ff","hj","jh","dsd"]

conn=sqlite3.connect('db.sqlite3')
cur=conn.cursor()


cur.executemany("INSERT INTO book_book VALUES(?,?,?,?,?,?,?,?);",vv)
conn.commit()
conn.close()
cur.execute("SELECT * FROM book_book;")
one_result=cur.fetchall()
print(one_result)
