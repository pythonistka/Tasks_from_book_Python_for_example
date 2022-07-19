import csv


def create():
    file = open("Users.csv", "r")
    new_name = input("Введите имя пользователя: ")
    reader = csv.reader(file)
    count = 0
    for row in file:
        if new_name in str(row):
            print("Данный пользователь уже существует")
            count = count + 1
    if count == 0:
        new_password = input("Введите пароль: ")
        new_record = new_name + ", " + new_password + "\n"
        file = open("Users.csv", "a")
        file.write(str(new_record))
    file.close()


def change():
    file = open("Users.csv", "r")
    change_name = input("Введите имя пользователя для изменения пароля: ")
    reader = csv.reader(file)
    for row in file:
        if change_name in str(row):
            file = list(csv.reader(open("Users.csv")))
            tmp = []
            for rows in file:
                tmp.append(rows)

            for step in tmp:
                if change_name in step:
                    step.clear()

            # file = open("Users.csv", "w")
            # x = 0
            # for liner in tmp:
            #     new_record = tmp[x][0] + ", " + tmp[x][1] + "\n"
            #     file.write(new_record)
            #     x = x + 1
            # file.close()
            #
            # new_password = input("Введите новый пароль: ")
            # new_record = change_name + ", " + new_password + "\n"
            # file = open("Users.csv", "a")
            # file.write(str(new_record))
            # file.close()


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
