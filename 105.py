import random


file = open("Numbers.txt", "w")
for i in range(1, 6):
    num = random.randint(1, 10)
    num = str(num)
    file.write(num + ", ")

file.close()
