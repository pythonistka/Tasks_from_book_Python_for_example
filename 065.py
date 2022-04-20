import turtle

turtle.shape("turtle")
turtle.pensize(3)
for i in range(0, 1):
    turtle.left(90)
    turtle.forward(120)
turtle.penup()
turtle.right(90)
turtle.forward(50)

turtle.pendown()
turtle.shape("turtle")
turtle.pensize(3)
for i in range(0, 1):
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(80)
turtle.penup()
turtle.forward(50)


turtle.pendown()
turtle.shape("turtle")
turtle.pensize(3)
for i in range(0, 1):
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(80)

turtle.exitonClick()