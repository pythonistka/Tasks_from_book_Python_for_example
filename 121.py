names = ["Игорь", "Иван"]


def add():
    add_name = input("Введите имя для добавления: ")
    names.append(add_name)
    return names


def change():
    for i in names:
        print(f"{names.index(i) + 1} {i}")
    change_num = int(input("Введите номер имени, которое хотите заменить: "))
    change_name = input("Введите новое имя: ")
    names[change_num - 1] = change_name
    for i in names:
        print(f"{names.index(i) + 1} {i}")
    return names


def remove():
    remove_name = input("Введите имя которое хотите удалить: ")
    names.remove(remove_name)
    return names


def show():
    for i in names:
        print(f"{names.index(i) + 1} {i}")
    print()


def main():
    run = True
    while run:
        print("\n" * 1)
        print("1) Добавить")
        print("2) Изменить")
        print("3) Удалить")
        print("4) Показать все")
        print("5) Завершить работу")
        select = int(input("Выберите номер команды: "))
        print("\n")
        if select == 1:
            add()
        elif select == 2:
            change()
        elif select == 3:
            remove()
        elif select == 4:
            show()
        elif select == 5:
            run = False
        else:
            print("Вы ввели неверную команду")


main()
