file = open("Names.txt", "r")
print(file.read())
file.close()

file = open("Names.txt", "r")
del_name = input("Введите имя из списка: ")
del_name = del_name + "\n"
for row in file:
    if row != del_name:
        file = open("Names2.txt", "a")
        new_names = row
        file.write(new_names)
        file.close()
file.close()

print("\n")

file = open("Names2.txt", "r")
print(file.read())
file.close()
