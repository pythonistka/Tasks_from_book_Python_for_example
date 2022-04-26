from array import *

new_array = array('i',[])
for x in range(1, 6):
    num = int(input("Введите число: "))
    new_array.append(num)

new_array = sorted(new_array)
new_array.reverse()

print(new_array)