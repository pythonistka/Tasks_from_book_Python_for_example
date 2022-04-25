upper = input("Введите слово, где все буквы будут с заглавной буквы: ")
again = False
while again == False:
    if upper.isupper():
        print("Спасибо!")
        again = True
    else:
        upper = input("Попробуйте еще раз: ")

