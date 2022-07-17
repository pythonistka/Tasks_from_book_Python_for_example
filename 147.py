import random


def start():
    color_list = ["1", "2", "3", "4", "5", "6"]
    print("Из заданного списка цветов, выбери 4:")
    print("[1] Красный")
    print("[2] Оранжевый")
    print("[3] Желтый")
    print("[4] Зеленый")
    print("[5] Голубой")
    print("[6] Фиолетовый")
    try_again = True
    while try_again == True:
        select_nums = list(input("Введи без пробелов номера выбранных цветов: "))
        t = 0
        for i in select_nums:
            t = t + 1
            if i not in color_list:
                print(f"Значение на {t} месте некорректно, цвет с таким номером не существует")
            else:
                try_again = False
    print("\n")
    print(select_nums)

    four_color_from_list = random.choices(color_list, k=4)
    print(four_color_from_list)

    correct = 0
    wrong_place = 0
    if select_nums[0] == four_color_from_list[0]:
        correct = correct + 1
    elif select_nums[0] == four_color_from_list[1] or select_nums[0] == four_color_from_list[2] or select_nums[0] == \
            four_color_from_list[3]:
        wrong_place = wrong_place + 1
    if select_nums[1] == four_color_from_list[1]:
        correct = correct + 1
    elif select_nums[1] == four_color_from_list[0] or select_nums[1] == four_color_from_list[2] or select_nums[1] == \
            four_color_from_list[3]:
        wrong_place = wrong_place + 1
    if select_nums[2] == four_color_from_list[2]:
        correct = correct + 1
    elif select_nums[2] == four_color_from_list[0] or select_nums[2] == four_color_from_list[1] or select_nums[2] == \
            four_color_from_list[3]:
        wrong_place = wrong_place + 1
    if select_nums[3] == four_color_from_list[3]:
        correct = correct + 1
    elif select_nums[3] == four_color_from_list[0] or select_nums[3] == four_color_from_list[1] or select_nums[3] == \
            four_color_from_list[2]:
        wrong_place = wrong_place + 1
    print(f"Правильных цветов на правильном месте:{correct}")
    print(f"Правильных цветов на неправильном месте:{wrong_place}")



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
