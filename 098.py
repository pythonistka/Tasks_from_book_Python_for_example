nums = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

line = int(input('Введите номер строки (от 0 до 3): '))
print(f"Данные из строки {line}: {nums [line]}")

new_num = int(input("Введите новое значение для добавления в строку: "))
nums[line].append(new_num)

print(f"Данные из обновленной строки {line}: {nums [line]}")
