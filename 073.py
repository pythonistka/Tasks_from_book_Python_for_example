dishes = {}
for i in range(1, 5):
    add_dish = input("Введите название любимого блюда: ")
    dishes[i] = add_dish
print(dishes)
del_dish = int(input("Введите номер блюда, которое вы хотите удалить: "))
del dishes[del_dish]

print(sorted(dishes.values()))

