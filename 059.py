import random

colours = random.choice(["красный", "оранжевый", "жёлтый", "зелёный", "голубой"])
answer = input("Угадайте цвет (красный, оранжевый, жёлтый, зелёный, голубой): ")
answer = answer.lower()
while colours != answer:
    hint = colours[3:len(colours)]
    print(f"Загаданный цвет окачивается на: {hint}")
    answer = input("Угадайте цвет (красный, оранжевый, жёлтый, зелёный, голубой): ")
print("Вы победили!")