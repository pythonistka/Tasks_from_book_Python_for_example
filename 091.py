from array import *

nums = array('i',[100, 50, 25, 50, 125])
print(nums)
num = int(input("Введите число из массива: "))
print(f'Число {num} встречается в массиве {nums.count(num)} раза')