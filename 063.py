import turtle

turtle.shape("turtle")
turtle.pensize(3)
turtle.color("black", "red")
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(90)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(150)


turtle.pendown()
turtle.shape("turtle")
turtle.pensize(3)
turtle.color("black", "yellow")
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(90)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(150)

turtle.pendown()
turtle.shape("turtle")
turtle.pensize(3)
turtle.color("black", "green")
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(90)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(150)

turtle.exitonClick()