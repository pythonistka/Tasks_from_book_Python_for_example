name = input("Введите ваше имя: ")
length_name = len(name)
control = 5
if length_name < control:
    surname = input('Введите вашу фамилию: ')
    total_name = name + surname
    total_name = total_name.upper()
    print(total_name)
else:
    name = name.lower()
    print(name)
