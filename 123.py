import csv


def add():
    file = open("Salaries.csv", "a")
    name = input("Введите имя: ")
    salary = input("Введите уровень зарплаты: ")
    new_info = name + ", " + salary + "\n"
    file.write(str(new_info))
    file.close()


def read():
    file = open("Salaries.csv", "r")
    for row in file:
        print(row)
    file.close()


def del_str():
    file = list(csv.reader(open("Salaries.csv")))
    x = 0
    tmp = []
    for row in file:
        tmp.append(row)

    for row in tmp:
        print(x, row)
        x = x + 1

    str_for_del = int(input("Введите номер строки для удаления: "))
    del tmp[str_for_del]

    file = open("Salaries.csv", "w")
    x = 0
    for row in tmp:
        new_record = tmp[x][0] + ", " + tmp[x][1] + "\n"
        file.write(new_record)
        x = x + 1
    file.close()


def main():
    run = True
    while run:
        print("\n" * 1)
        print("1) Добавить данные в файл")
        print("2) Вывести все данные из файла")
        print("3) Удалить запись из файла")
        print("4) Завершить работу")
        select = int(input("Выберите номер команды: "))
        print("\n")
        if select == 1:
            add()
        elif select == 2:
            read()
        elif select == 3:
            del_str()
        elif select == 4:
            run = False
        else:
            print("Вы ввели отсутствующую команду")


main()
