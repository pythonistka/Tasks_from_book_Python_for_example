num = int(input("Введите число от 10 до 20: "))
num_min = 10
num_max = 20
while num > num_max or num < num_min:
    if num > num_max:
        print("Слишком высокое число")
    elif num < num_min:
        print("Слишком низкое число")
    num = int(input("Попробуй еще: "))
print("Спосебо")
