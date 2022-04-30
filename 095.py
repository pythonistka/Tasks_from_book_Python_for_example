from array import *

nums = array('f', [20.05, 30.06, 40.07, 50.08, 60.09])
num = int(input("Введите число в диапазоне от 2 до 5: "))
while num > 5 or num < 2:
    num = int(input("Ошибка, попробуй еще раз: "))
else:
    for i in nums:
        div_num = round((i / num), 2)
        print(div_num)