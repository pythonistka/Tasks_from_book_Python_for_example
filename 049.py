count = 1
compun = 50
num = int(input("Введите число: "))
while num != compun:
    if num > compun:
        print(f"{num} больше правильного числа")
        num = int(input("Введите число: "))
        count = count + 1
    elif num < compun:
        print(f"{num} меньше правильного числа")
        num = int(input("Введите число: "))
        count = count + 1
print(f"Вы победили c {count} попытки!")

