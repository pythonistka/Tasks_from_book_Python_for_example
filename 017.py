age = int(input("Введите ваш возраст: "))
vote = 18
drive = 17
lottery = 16

if age >= vote:
    print("Вы можете голосовать")
elif age == drive:
    print("Вы можете учиться водить машину")
elif age == lottery:
    print("Вы можете покупать лотерейные билеты")
else:
    print("Вы можете выпрашивать сладости")
    