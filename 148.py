import csv


def get_data():
    file = list(csv.reader(open("Users.csv")))
    tmp = []
    for x in file:
        tmp.append(x)
    return tmp


def create_user_id(tmp):
    name_again = True
    while name_again:
        user_id = input("Введите имя пользователя: ")
        user_id.lower()
        inlist = False
        row = 0
        for y in tmp:
            if user_id in tmp[row][0]:
                print("Данный пользователь уже существует")
                inlist = True
            row = row + 1
        if not inlist:
            name_again = False
    return user_id


def create_password():
    symbol_list = ["!", "£", "$", "%", "^", "&", "*", "(", ")", "?", "@", "#"]
    num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    try_again = True
    while try_again:
        score = 0
        low_sym = False
        up_sym = False
        symbol_in = False
        number_in = False
        password = input("Введите пароль: ")
        lenght = len(password)
        if lenght >= 8:
            score = score + 1
        for x in password:
            if x.islower():
                low_sym = True
            if x.isupper():
                up_sym = True
            if x in symbol_list:
                symbol_in = True
            if x in num_list:
                number_in = True
        if low_sym == True:
            score = score + 1
        if up_sym == True:
            score = score + 1
        if symbol_in == True:
            score = score + 1
        if number_in == True:
            score = score + 1
        if score == 1 or score == 2:
            print("Ненадежный пароль, попробуй еще раз")
        elif score == 3 or score == 4:
            print("Умеренно надежный пароль")
            again = input("Попробуешь усложнить пароль?(да/нет): ")
            again.lower()
            if again == "нет":
                try_again = False
        password_repeat = input("Повторите пароль: ")
        if password_repeat != password:
            print("Пароли не совпадают")
            main()
        else:
            return password


def search_name(tmp):
    ask_name = True
    user_id = ""
    while ask_name == True:
        search_id = input("Введите имя для поиска: ")
        search_id.lower()
        inlist = False
        row = 0
        for y in tmp:
            if search_id in tmp[row][0]:
                inlist = True
            row = row + 1
        if inlist == True:
            user_id = search_id
            ask_name = False
        else:
            print("Такого имени нет в списке")
    return user_id


def change(user_id, tmp):
    if user_id != "":
        password = create_password()
        id = user_id.index(user_id)
        tmp[id][1] = password
        file = open("Users.csv", "w")
        x = 0
        for row in tmp:
            newrec = tmp[x][0] + ", " + tmp[x][1] + "/n"
            file.write(newrec)
            x = x + 1
        file.close()


def display(tmp):
    x = 1
    for row in tmp:
        print(x, row)
        x = x + 1


def main():
    tmp = get_data()
    run = True
    while run:
        print("[1] Создать нового пользователя")
        print("[2] Изменить пароль")
        print("[3] Показать всех пользователей")
        print("[4] Уйти")
        select = int(input("Введите номер команды: "))
        if select == 1:
            user_id = create_user_id(tmp)
            password = create_password()
            file = open("Users.csv", "a")
            new_record = user_id + ", " + password + "\n"
            file.write(str(new_record))
            file.close()
        elif select == 2:
            user_id = search_name(tmp)
            change(user_id, tmp)
        elif select == 3:
            display(tmp)
        elif select == 4:
            run = False
        else:
            print("Вы ввели несуществующее действие, попробуйте еще раз")


main()
