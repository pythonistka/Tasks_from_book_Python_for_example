import math

print("1) Квадрат")
print("2) Треугольник")
num_1 = 1
num_2 = 2
enter_num = int(input("Введите номер: "))
if enter_num == num_1:
    side_of_square = int(input("Введите длину стороны квадрата: "))
    area_square = side_of_square**2
    print(f"Площадь кадрата равна: {area_square}")
elif enter_num == num_2:
    side_of_triangle = int(input("Введите длину стороны треугольника: "))
    hight_of_triangle = int(input("Введите высоту треугольника: "))
    area_triangle = 0.5 * side_of_triangle * hight_of_triangle
    print(f"Площадь треугольника равна: {area_triangle}")
else:
    print(f"Ввести можно только 1 или 2, проверьте правильность введенных данных")
