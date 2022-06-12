import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()


cursor.execute("""INSERT INTO Books(title, author, datepublished)
VALUES("Harry Potter and the prisoner of Azkaban", "J. K. Rowling", "1999")""")
db.commit()

cursor.execute("""INSERT INTO Books(title, author, datepublished)
VALUES("Lyrebird", "Cecelia Ahern", "2017")""")
db.commit()

cursor.execute("""INSERT INTO Books(title, author, datepublished)
VALUES("Murder on the Orient Express", "Agatha Christie", "1934")""")
db.commit()

cursor.execute("""INSERT INTO Books(title, author, datepublished)
VALUES("Perfect", "Cecelia Ahern", "2017")""")
db.commit()

cursor.execute("""INSERT INTO Books(title, author, datepublished)
VALUES("The marble collector", "Cecelia Ahern", "2016")""")
db.commit()


cursor.execute("""INSERT INTO Books(title, author, datepublished)
VALUES("The murder on the links", "Agatha Christie", "1923")""")
db.commit()

cursor.execute("""INSERT INTO Books(title, author, datepublished)
VALUES("The picture of Dorian Gray", "Oscar Wilde", "1890")""")
db.commit()

cursor.execute("""INSERT INTO Books(title, author, datepublished)
VALUES("The secret adversary", "Agatha Christie", "1921")""")
db.commit()

cursor.execute("""INSERT INTO Books(title, author, datepublished)
VALUES("The seven dials mystery", "Agatha Christie", "1929")""")
db.commit()

cursor.execute("""INSERT INTO Books(title, author, datepublished)
VALUES("The year I met you", "Cecelia Ahern", "2014")""")
db.commit()

cursor.execute("SELECT * FROM Books")
for x in cursor.fetchall():
    print(x)

db.close()