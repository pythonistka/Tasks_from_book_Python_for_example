import turtle
import random

turtle.shape("turtle")
turtle.pensize(3)
for i in range(0, 8):
    turtle.color(random.choice(["red", "black", "green", "blue", "orange","yellow", "brown"]))
    turtle.right(45)
    turtle.forward(120)
turtle.exitonClick()