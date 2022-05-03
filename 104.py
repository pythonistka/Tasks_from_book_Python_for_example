people = {}
for i in range(1, 3):
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    size = int(input("Введите размер обуви: "))
    people[name] = {"Age": age, "Size": size}

del_human = input("Введите имя для удаления из списка: ")
del people[del_human]

for name in people:
    print((name), people[name]["Age"], people[name]["Size"])