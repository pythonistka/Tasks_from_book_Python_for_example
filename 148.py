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
    symbol_list = ["!", "£", "$", "%", "^", "&", "*", "(",")", "?", "@", "#"]
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
            again = input("Попробуешь еще раз?(да/нет): ")
            again.lower()
            if again != "нет":
                continue
            try_again = False
    else:
            return password


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
            change_password = input("Введите новый пароль: ")
            ID = change_name.index(change_name)
            tmp[ID][1] = change_password
            print(tmp[ID][1])
            file = open("Users.csv", "w")
            x = 0
            for step in tmp:
                new_record = tmp[x][0] + ", " + tmp[x][1] + "\n"
                file.write(new_record)
                x = x + 1
            file.close()


def display():
    file = open("Users.csv", "r")
    reader = csv.reader(file)
    x = 1
    for row in reader:
        print(x, row)
        x = x + 1
    file.close()


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
            change()
        elif select == 3:
            display()
        elif select == 4:
            run = False
        else:
            print("Вы ввели несуществующее действие, попробуйте еще раз")


main()
