import csv

file = open("Books.csv", "a")
how_many_row = int(input('Как много строк вы желаете добавить?: '))
for i in range(0, how_many_row):
    book = input("Введите название книги: ")
    name = input("Введите имя писателя: ")
    year = input("Введите год: ")
    new_info = book + ", " + name + ", " + year + "\n"
    file.write(str(new_info))
file.close()

file = open("Books.csv", "r")
search = input('Произведения какого автора вас интересуют?: ')
reader = csv.reader(file)
count = 0
for row in file:
    if search in str(row):
        print(row)
        count = count + 1
if count == 0:
    print('Писатель не найден')
file.close()





