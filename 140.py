import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()


def view():
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)


def add():
    new_firstname = input("Введите имя: ")
    new_surname = input("Введите фамилию: ")
    new_phonenumber = input("Введите номер телефона: ")
    cursor.execute("""INSERT INTO Names(firstname, surname, phonenumber)
    VALUES(?, ?, ?)""", (new_firstname, new_surname, new_phonenumber))
    db.commit()


def search():
    search_surname = input("Введите фамилию для поиска: ")
    cursor.execute("SELECT * FROM Names WHERE surname = ?", [search_surname])
    for x in cursor.fetchall():
        print(x)


def delete_data():
    delete_id = int(input("Введите ID для удаления записи из телефонной книги: "))
    cursor.execute("DELETE FROM Names WHERE id = ?", [delete_id])
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)
    db.commit()


def main():
    run = True
    while run:
        print("Меню")
        print("\n" * 1)
        print("1) Показать всю телефонную книгу")
        print("2) Добавить запись в телефонную книгу")
        print("3) Поиск по фамилии")
        print("4) Удалить запись из книги")
        print("5) Завершить")
        print("\n" * 1)
        select = int(input("Введите номер операции: "))
        print("\n" * 1)
        if select == 1:
            view()
        elif select == 2:
            add()
        elif select == 3:
            search()
        elif select == 4:
            delete_data()
        elif select == 5:
            run = False
        else:
            print("Проверьте корректность введенной команды")


main()
