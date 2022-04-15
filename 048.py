counter = 0
question = "да"
while question == "да":
    name_add = input("Введите имя человека, которого хотите приглазить на вечеринку: ")
    print(f'{name_add} добавлен в список')
    counter = counter + 1
    question = input("Хотите пригласить кого-то еще?(да/нет): ")
print(f"На вечеринке будет: {counter} человек")

