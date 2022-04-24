telecast = ["Давай поженимся", "Топгир", "Очумелые ручки", "Царь горы"]
for i in telecast:
    print(i)
tv_length = len(telecast) - 1
name_tv = input("Введите дополнительное название телеперадачи: ")
tv_position = int(input(f"На какой позиции она должна находиться? от 0 до {tv_length}: "))
telecast.insert(tv_position, name_tv)
for i in telecast:
    print(i)