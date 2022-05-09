import csv

file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)

x = 0
for row in tmp:
    print(x, row)
    x = x + 1

del_str = int(input("Какую строку вы хотите удалить?: "))
del tmp[del_str]

print("Новый массив данных:")
x = 0
for row in tmp:
    print(x, row)
    x = x + 1

line = int(input('Введите номер строки, в которой хотите изменить данные: '))
print(f"Данные из строки {line}: {tmp [line]}")

column = int(input(f'Введите номер столбца (от 0 до 2), в котором хотите изменить данные из строки {line}: '))
print(f"Значение из строки {line} и колонки {column}: {tmp [line] [column]}")

new_value = (input("Введите новое значение: "))
tmp [line] [column] = new_value
print(f"Строка с новыми данными:{tmp[line]}")

file = open("Books.csv", "w")
x = 0
for row in tmp:
    new_record = tmp [x][0] + ", " + tmp [x][1] + ", " + tmp [x][2] + "\n"
    file.write(new_record)
    x = x + 1
file.close()