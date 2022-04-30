from array import *

nums = array('i', [100, 50, 25, 75, 125])

for i in nums:
    print(i)

num = int(input("Введите число из массива: "))
while num not in nums:
    num = int(input("Попробуй еще раз: "))
else:
    print(f"Позиция выбранного числа в массиве: {nums.index(num)}")