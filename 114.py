import csv

file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)

search_start = int(input('Введите начальный год: '))
search_end = int(input('Введите конечный год: '))

x = 0
for row in tmp:
    if search_start <= int(tmp[x][2]) <= search_end:
        print(tmp[x])
    x = x + 1
