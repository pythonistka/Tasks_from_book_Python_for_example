names = ["Игорь", "Иван"]

def add():
    add_name = input("Введите имя для добавления: ")
    names.append(add_name)

def change():
    for i in names:
    print(f"{names.index(i)+1} {i}")

def remove():
    remove_name = input("Введите имя которое хотите удалить: ")
    names.remove(remove_name)

def main():
    print("1) Добавить")
    print("2) Изменить")
    print("3) Удалить")
    print("4) Показать все")
    print("5) Завершить работу")
    select = int(input("Выберите номер команды: "))


