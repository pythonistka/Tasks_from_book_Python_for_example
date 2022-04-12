import math

radius = int(input("Введите радиус цилиндра: "))
hight = int(input("Введите высоту цилиндра: "))

volume = round((math.pi * radius**2 * hight),3)

print(f"Объем цилиндра равен: {volume}")
