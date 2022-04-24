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
print(f"Вы пригласили {len(guests)} гостей: {guests}")
name_show = input("Введите одно из имен в списке: ")
print(f"Позиция гостя в списке: {guests.index(name_show)}")
answer = input("Хотите чтоб этот человек присутствовал на вечеринке? (да/нет): ")
if answer == "нет":
    del guests[guests.index(name_show)]
print(f'На вечеринке будут присутствовать :{guests}')