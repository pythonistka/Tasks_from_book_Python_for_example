import csv


def create():
    file = open("Users.csv", "a")
    new_record = "Oleg, Oleg21\n"
    file.write(str(new_record))
    file.close()


def change():
    pass


def display():
    file = open("Users.csv", "r")
    reader = csv.reader(file)
    x = 1
    for row in reader:
        print(x, row[0])
        x = x + 1
    file.close()


def main():
    run = True
    while run:
        print("[1] Создать нового пользователя")
        print("[2] Изменить пароль")
        print("[3] Показать всех пользователей")
        print("[4] Уйти")
        select = int(input("Введите номер команды: "))
        if select == 1:
            create()
        elif select == 2:
            change()
        elif select == 3:
            display()
        elif select == 4:
            run = False
        else:
            print("Вы ввели несуществующее действие, попробуйте еще раз")


main()