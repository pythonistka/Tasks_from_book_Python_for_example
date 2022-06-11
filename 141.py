import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Books(
id integer PRIMARY KEY,
title text NOT NULL,
author text NOT NULL,
datepublished integer);""")

cursor.execute("""INSERT INTO Books(title, author, datepublished)
VALUES("De Profundis", "Oscar Wilde", "1905")""")
db.commit()


cursor.execute("SELECT * FROM Books")
for x in cursor.fetchall():
    print(x)

db.close()