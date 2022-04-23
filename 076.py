guests = []
x = 3
for i in range(1,4):
    name = input("Введите имя гостя: ")
    guests.append(name)
while len(guests) >= x:
    answer = input("Хотите позвать еще гостей (да/нет): ")
    if answer == "да":
        name = input("Введите имя гостя: ")
        guests.append(name)
    else:
        break
print(f"Вы пригласили: {len(guests)} гостей")