import random
import csv

score = 0
name = input("Введите ваше имя: ")
num_1 = random.randint(1, 10)
num_2 = random.randint(1, 10)
question_1 = str(num_1) + "+" + str(num_2) + "="
ans_1 = int(input(question_1))
real_ans_1 = num_1 + num_2

if ans_1 == real_ans_1:
    score = score + 1

num_3 = random.randint(1, 10)
num_4 = random.randint(1, 10)
question_2 = str(num_3) + "+" + str(num_4) + "="
ans_2 = int(input(question_2))
real_ans_2 = num_3 + num_4

if ans_2 == real_ans_2:
    score = score + 1

file = open("Questions.csv", "a")
new_record = name + ", " + question_1 + str(ans_1) + ", " + question_2 + str(ans_2) + ", " + str(score) + "\n"
file.write(str(new_record))

file.close()
