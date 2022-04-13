answer = input("В каком направлении вести отсчёт, в прямом или обратном?(п/о): ")
answer_1 = "п"
answer_2 = "о"
if answer == answer_1:
    num = int(input("Введите число: "))
    for i in range(1, num + 1):
        print(i)
elif answer == answer_2:
    num = int(input("Введите число меньше 20: "))
    for i in range(20, num - 1, -1):
        print(i)
else:
    print("Я вас не понимаю")