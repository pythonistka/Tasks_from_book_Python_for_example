import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

print()
date_of_public = int(input("Введите год: "))
print()

cursor.execute("""SELECT Books.title, Books.datepublished, Books.author
 FROM Books WHERE datepublished > ? ORDER BY datepublished """, [date_of_public])
for x in cursor.fetchall():
    print(x)