num = int(input("Введите число от 1 до 12: "))
num_1 = 1
num_12 = 12
if num_1 < num < num_12:
    for i in range (1, 11):
        answer = num * i
        print(num, "x", i, "=", answer)
else:
    print("Ваше число не соответствует заданному критерию")