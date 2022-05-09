import csv

file = open("Books.csv", "r")
x = 0
for row in file:
    print(f"В строке:{x}, содержится запись: {row}")
    x = x + 1