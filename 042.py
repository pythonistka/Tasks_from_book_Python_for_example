total = 0
answer_sum = "да"
for i in range(0, 5):
    num = int(input("Введите число: "))
    answer = input("Хотите вкючить данное число в суммирование? (да/нет): ")
    if answer == answer_sum:
        total = total + num
    else:
        total = total
print(f"Результат суммирования: {total}")
