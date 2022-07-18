

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