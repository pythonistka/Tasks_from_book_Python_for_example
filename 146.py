alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
            "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", " "]


def make_code():
    text = (input("Введите текст для кодировки: "))
    num = int(input("Введите коэффициент кодировки от 1 до 33: "))
    text = text.lower()
    while num > 33 or num == 0:
        print("Число не входит в требуемый диапазон, попробуй еще раз")
        num = int(input("Введите коэффициент кодировки от 1 до 33: "))

    text_code = ""
    for x in text:
        y = alphabet.index(x)
        y_code = y + num
        if y_code > 32:
            y_code = y_code - 33
        letter = alphabet[y_code]
        text_code = text_code + letter
    print(text_code.title())


def decode():
    text = (input("Введите текст для раскодировки: "))
    num = int(input("Введите коэффициент раскодировки от 1 до 33: "))
    text = text.lower()
    while num > 33 or num == 0:
        print("Число не входит в требуемый диапазон, попробуй еще раз")
        num = int(input("Введите коэффициент кодировки от 1 до 33: "))

    text_decode = ""
    for x in text:
        y = alphabet.index(x)
        y_decode = y - num
        if y_decode < 0:
            y_decode = y_decode + 33
        letter = alphabet[y_decode]
        text_decode = text_decode + letter
    print(text_decode.title())


def main():
    run = True
    while run:
        print("\n")
        print("1) Закодировать текст")
        print("2) Раскодировать текст")
        print("3) Завершить")
        print("\n")
        select = int(input("Выберите действие: "))
        print("\n")
        if select == 1:
            make_code()
        elif select == 2:
            decode()
        elif select == 3:
            run = False
        else:
            print("Проверьте корректность ввода команды")
            print("\n")


main()
