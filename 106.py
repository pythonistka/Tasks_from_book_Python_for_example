file = open("Names.txt", "w")

names = ["Инна", "Олег", "Иван", "Казимир", "Умиджон"]
for i in names:
    file.write(i + "\n")

file.close()