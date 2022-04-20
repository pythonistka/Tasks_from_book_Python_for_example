import turtle
import random

turtle.shape("turtle")
turtle.pensize(3)

lines = random.randint(5, 20)

for i in range(0, lines):
    turtle.color(random.choice(["red", "black", "green", "blue", "orange", "yellow", "brown"]))
    lenght = random.randint(25, 100)
    rotate = random.randint(1, 365)
    turtle.forward(lenght)
    turtle.right(rotate)

turtle.exitonClick()