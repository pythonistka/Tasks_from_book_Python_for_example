import random

num = random.randint(1, 10)
answer = 0
while answer != num:
    answer = int(input("Угадай число от 1 до 10: "))
print("Ты угадал!")