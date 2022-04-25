password = input("Введите пароль: ")
password_repeat = input("Введите пароль еще раз: ")
if password == password_repeat:
    print("Спосебо!")
elif password.lower() == password_repeat.lower():
    print("Буквы должны быть в одном регистре")
else:
    print("Некорректно")