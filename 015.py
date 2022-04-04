colour = input('Введите ваш любимый цвет: ')
colour = colour.lower()
correct_colour = "красный"
if colour == correct_colour:
    print(f"Я тоже люблю {correct_colour} цвет")
else:
    print(f"Я не люблю {colour} цвет, я люблю {correct_colour}")