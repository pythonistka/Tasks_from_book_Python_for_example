people = int(input("Сколько гостей вы хотите пригласить на вечеринку?: "))
num = 10
if people < num:
    for i in range(1, people + 1):
        name = input(f"Введите имя {i} гостя: ")
        print(f"{name} добавлен в список гостей")
else:
    print("Слишком много людей")

