import random


def start():
        print("Из заданного списка цветов, выбери 4:")
        print("[1] Красный")
        print("[2] Оранжевый")
        print("[3] Желтый")
        print("[4] Зеленый")
        print("[5] Голубой")
        print("[6] Фиолетовый")
        select_nums = []
        select_nums = input("Введи поочередно, через запятую выбранные цвета: ")
        print("\n")
        print(select_nums)

        color_list = [1, 2, 3, 4, 5, 6]
        four_color_from_list = random.choices(color_list, k=4)
        print(four_color_from_list)


pass


def rule():
    print("Компьютер автоматически генерирует комбинацию из четырех цветов из списка возможных.""\n"
          "Вы вводите комбинацию из четырех цветов из списка, использованного компьютером.""\n"
          "Программа сообщает, сколько цветов находятся в правильной позиции и сколько правильно угаданных цветов "
          "находятся в неправильных позициях.""\n"
          "Вы продолжаете гадать, пока не введете все четыре цвета в правильном порядке"
          )
    pass


def main():
    x = 0
    while x == 0:
        print("\n")
        print("1) Правила")
        print("2) Играть")
        print("3) Уйти")
        select = int(input("Выберите номер команды: "))
        print("\n")
        if select == 1:
            rule()
            x = 0
        elif select == 2:
            start()
            x = x + 1
        elif select == 3:
            break
        else:
            print("Вы ввели неверную команду")
            x = 0


main()
