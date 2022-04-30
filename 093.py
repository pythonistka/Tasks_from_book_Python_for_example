from array import *

nums = array('i', [])
new_nums = array('i', [])

for i in range (1, 6):
    num = int(input("Введите число: "))
    nums.append(num)

nums = sorted(nums)

for x in nums:
    print(x)

del_num = int(input("Выберите одно из чисел: "))
if del_num in nums:
    nums.remove(del_num)
    new_nums.append(del_num)
    print(nums)
    print(new_nums)
else:
    print("Выбранное число в диапазон не входит")
