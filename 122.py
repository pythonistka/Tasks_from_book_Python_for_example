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


def main():
    run = True
    while run:
        print("\n" * 1)
        print("1) Добавить данные в файл")
        print("2) Вывести все данные из файла")
        print("3) Завершить работу")
        select = int(input("Выберите номер команды: "))
        print("\n")
        if select == 1:
            add()
        elif select == 2:
            read()
        elif select == 3:
            run = False
        else:
            print("Вы ввели отсутствующую команду")


main()

