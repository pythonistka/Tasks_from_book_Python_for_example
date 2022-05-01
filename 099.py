nums = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

line = int(input('Введите номер строки (от 0 до 3): '))
print(f"Данные из строки {line}: {nums [line]}")

column = int(input(f'Введите номер столбца (от 0 до 2) из строки {line}: '))
print(f"Значение из строки {line} и колонки {column}: {nums [line] [column]}")

answer = input("Желаете изменить данное значение? (да/нет): ")
if answer == "да":
    new_num = int(input("Введите новое значение: "))
    nums [line] [column] = new_num
    print(f"Строка с новыми данными:{nums[line]}")
else:
    print(f"Строка без изменений:{nums[line]}")
