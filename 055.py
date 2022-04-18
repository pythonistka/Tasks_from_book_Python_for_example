import random

num = random.randint(1, 5)
answer = int(input("Угадай число: "))
if answer == num:
    print("Вы победитель!")
elif answer != num:
    if answer > num:
        print("Ваше число больше!")
    if answer < num:
        print("Ваше число меньше!")
    answer = int(input("Попробуй еще: "))
    if answer == num:
        print("Верно!")
    else:
        print("Вы лузер :(")

