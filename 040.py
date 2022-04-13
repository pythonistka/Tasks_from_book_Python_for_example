num = int(input("Введите число от 1 до 50: "))
num_1 = 1
num_50 = 50
if num_1 < num < num_50:
    for i in range(num_50, num - 1, -1):
        print(i)
else:
    print("Ваше число не соответствует заданному критерию")
