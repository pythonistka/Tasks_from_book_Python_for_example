import csv

file = open("Books.csv", "r")
x = 0
for row in file:
    print(x, row)
    x = x + 1