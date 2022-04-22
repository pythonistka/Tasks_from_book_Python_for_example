num_list = [123, 456, 789, 147]
for i in num_list:
    print(i)

input_num = int(input("Ваедите трехзначное число: "))
if input_num in num_list:
    print(f"Введенное вами число имеет индекс: {num_list.index(input_num)}")
else:
    print("Введенное вами число отсутствует в списке")