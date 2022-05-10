import random
import csv

file = open("Questions.csv", "a")
name = input("Ввелите ваше имя: ")
question_1 = int(input(random.choice(["Сколько вам лет?: ", "Какого вы года рождения?: "])))
question_2 = input(random.choice(["У вас есть домашнее животное?: ", "Вы замужем?: "]))
new_record = name + ", " + question_1 + ", " + question_2 + "\n"
file.write(str(new_record))
file.close()
