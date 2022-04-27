from array import *
import random

new_array = array('i',[])
for x in range (1, 6):
    num = random.randint(0, 100)
    new_array.append(num)
for x in new_array:
    print(x)


