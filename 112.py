import csv

file = open("Books.csv", "a")
book = input("Введите название книги: ")
name = input("Введите имя писателя: ")
year = input("Введите год: ")
new_info = book + ", " + name + ", " + year + "\n"
file.write(str(new_info))
file.close()

file = open("Books.csv", "r")
for row in file:
    print(row)