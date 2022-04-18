import random

num = random.randint(1, 10)
answer = 0
while answer != num:
    answer = int(input("Угадай число от 1 до 10: "))
    if answer > num:
        print("Ваше число больше!")
    elif answer < num:
        print("Ваше число меньше!")
print("Ты угадал!")