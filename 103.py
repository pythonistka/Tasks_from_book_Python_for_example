people = {}
for i in range(1, 3):
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    size = int(input("Введите размер обуви: "))
    people[name] = {"Age": age, "Size": size}


for name in people:
    print((name), people[name]["Age"])