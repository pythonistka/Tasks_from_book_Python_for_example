import turtle

turtle.shape("turtle")
turtle.pensize(3)
turtle.color("black", "red")
for i in range(0, 5):
    turtle.forward(90)
    turtle.right(30)
    turtle.forward(90)
    turtle.left(102)
turtle.exitonClick()