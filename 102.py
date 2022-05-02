people = {}
for i in range(1, 5):
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    size = int(input("Введите размер обуви: "))
    people[name] = {"Age": age, "Size": size}


search = input("Введите имя, чьи данные необходимы: ")
print(people[search])