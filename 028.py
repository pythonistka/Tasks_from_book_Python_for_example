num = float(input('Введите число с большим количеством знаков в дробной части: '))
coefficient = int(input("Введите коэффициент для умножения вашего числа: "))
result = round((num * coefficient), 2)

print(f'Ваше число умноженное на {coefficient}: {result}')