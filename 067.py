import turtle
import random

turtle.shape("turtle")
turtle.pensize(3)
for i in range(0, 10):
    turtle.color(random.choice(["red", "black", "green", "blue", "orange", "yellow", "brown"]))
    for x in range (0, 8):
        turtle.forward(50)
        turtle.right(45)
    turtle.right(36)
turtle.exitonClick()