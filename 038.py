name = input("Введите ваше имя: ")
num = int(input("Введите число: "))
print(f"Выводим ваше имя по буквам {num} раз:")
for i in range (0, num):
    for x in name:
        print(x)