name = input("Введите ваше имя: ")
num = int(input("Введите число: "))
num_for_range = num + 1
print(f"Выводим ваше имя {num} раз:")

for i in range(1, num_for_range):
    print(name)