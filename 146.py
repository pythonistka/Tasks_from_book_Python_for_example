







def main():
    run = True
    while run:
        print("\n")
        print("1) Закодировать текст")
        print("2) Раскодировать текст")
        print("3) Завершить")
        print("\n")
        select = int(input("Выберите действие: "))
        if select == 1:
            make_code()
        elif select == 2:
            decode()
        elif select == 3:
            run = False
        else:
            print("Проверьте корректность ввода команды")


main()