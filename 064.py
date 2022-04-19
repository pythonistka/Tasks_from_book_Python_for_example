import turtle

turtle.shape("turtle")
turtle.pensize(3)
turtle.color("black", "red")
turtle.begin_fill()
for i in range(0, 5):
    turtle.forward(100)
    turtle.right(144)
turtle.penup()
turtle.end_fill()
turtle.exitonClick()