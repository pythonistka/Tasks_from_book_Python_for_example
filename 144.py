import sqlite3

file = open("BookInfo.txt", "w")

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("""SELECT name from authors""")
for x in cursor.fetchall():
    print(x)

print()
name_of_author = input("Введите имя автора: ")
print()

cursor.execute("""SELECT Books.id, Books.title, Books.author, Books.datepublished
 FROM Books WHERE author = ?""", [name_of_author])
for x in cursor.fetchall():
    new_rec = str(x[0]) + " - " + x[1] + " - " + x[2] + " - " + str(x[3]) + "\n"
    file.write(new_rec)

file.close()

db.close()

file = open("BookInfo.txt", "r")
print(file.read())
file.close()