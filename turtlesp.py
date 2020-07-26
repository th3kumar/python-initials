import turtle
import random

turtle.shape("turtle")
turtle.pensize(5)

for x in range(0,10):
    for i in range(0,8):
        turtle.color(random.choice(["red","yellow","blue","green","orange"]))
        turtle.forward(50)
        turtle.right(45)
    turtle.right(36)

turtle.exitonclick()
