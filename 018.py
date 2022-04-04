number = int(input('Введите число: '))
if number < 10:
    print('Слишком маленькое')
elif 10 <= number <= 20:
    print('Угадали')
else:
    print('Слишком большое')
