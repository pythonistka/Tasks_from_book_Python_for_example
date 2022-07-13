






def main():
    color_list = [1, 2, 3, 4, 5, 6]
    run = True
    while run:
        print("\n" * 1)
        print("Из заданного списка цветов, выбери 4:")
        print("[1] Красный")
        print("[2] Оранжевый")
        print("[3] Желтый")
        print("[4] Зеленый")
        print("[5] Голубой")
        print("[6] Фиолетовый")
        select = []
        select = int(input("Введи поочередно, через запятую выбранные цвета: "))
        print("\n")
        print(select)