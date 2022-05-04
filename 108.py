file = open("Names.txt", "a")
new_name = input("Введите имя для добавления: ")
file.write(new_name + "\n")
file.close()

file = open("Names.txt", "r")
print(file.read())
file.close()