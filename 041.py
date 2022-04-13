name = input("Введите ваше имя: ")
num = int(input("Введите число: "))
num_1 = 1
num_10 = 10
message = "Слишком большое число"
if num < num_10:
    for i in range(0, num):
        print(name)
else:
    for i in range(0, 3):
        print(message)