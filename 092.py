from array import *
import random

nums = array('i',[])
random_nums = array('i',[])

for x in range (1, 4):
    num = int(input("Введите число: "))
    nums.append(num)

for y in range (1, 6):
    random_num = random.randint(0, 200)
    random_nums.append(random_num)

new_nums = sorted(nums + random_nums)

for i in new_nums:
    print(i)



