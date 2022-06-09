import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Authors(
name text PRIMARY KEY,
plaseofbirth text NOT NULL);""")

cursor.execute("""INSERT INTO Authors(name, plaseofbirth)
VALUES("Agatha Christie", "Torquay")""")
db.commit()

cursor.execute("""INSERT INTO Authors(name, plaseofbirth)
VALUES("Cecelia Ahern", "Dublin")""")
db.commit()

cursor.execute("""INSERT INTO Authors(name, plaseofbirth)
VALUES("J. K. Rowling", "Bristol")""")
db.commit()

cursor.execute("""INSERT INTO Authors(name, plaseofbirth)
VALUES("Oscar Wilde", "Dublin")""")
db.commit()

cursor.execute("SELECT * FROM Authors")
for x in cursor.fetchall():
    print(x)

db.close()