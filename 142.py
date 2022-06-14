import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT * FROM Authors")
for x in cursor.fetchall():
    print(x)

print()
plase_of_birth = input("Введите место рождения автора: ")
print()

cursor.execute("""SELECT Books.title, Books.datepublished, Books.author
 FROM Books, Authors WHERE Authors.name = Books.author AND Authors.plaseofbirth = ?""", [plase_of_birth])
for x in cursor.fetchall():
    print(x)

db.close()