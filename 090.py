from array import *

new_array = array('i',[])
while len(new_array) < 5:
    num = int(input("Введите число: "))
    if 10 <= num <= 20:
        new_array.append(num)
    else:
        print("Число не входит в диапазон")
print("Спасибо!")
for i in new_array:
    print(i)