import math

num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
result = num_1 // num_2
remainder = num_1 % num_2

print(f"Если разделить {num_1} на {num_2}, получится {result} с остатком {remainder}")