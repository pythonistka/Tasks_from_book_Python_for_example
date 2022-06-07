import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Names(
id integer PRIMARY KEY,
firstname text NOT NULL,
surname text NOT NULL,
phonenumber integer);""")

cursor.execute("""INSERT INTO Names(firstname, surname, phonenumber)
VALUES("Simon", "Howies", "01223 349752")""")
db.commit()

cursor.execute("""INSERT INTO Names(firstname, surname, phonenumber)
VALUES("Karen", "Phillips", "01954 295773")""")
db.commit()

cursor.execute("""INSERT INTO Names(firstname, surname, phonenumber)
VALUES("Darren", "Smith", "01583 749012")""")
db.commit()

cursor.execute("""INSERT INTO Names(firstname, surname, phonenumber)
VALUES("Anne", "Jones", "01323 567322")""")
db.commit()

cursor.execute("""INSERT INTO Names(firstname, surname, phonenumber)
VALUES("Mark", "Smith", "01223 855534")""")
db.commit()

db.close()