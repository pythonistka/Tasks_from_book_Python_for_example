import random

attempt = 0
for i in range(1, 6):
    num_1 = random.randint(0, 10)
    num_2 = random.randint(0, 10)
    print(f"Сколько будет: {num_1} + {num_2}?")
    answer = int(input("Введите ответ: "))
    correct = num_1 + num_2
    if answer == correct:
        attempt = attempt + 1
    else:
        attempt = attempt
print(f"Количество правильных ответов: {attempt}")


