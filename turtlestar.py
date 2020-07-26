import turtle
import random

turtle.shape("turtle")
turtle.pensize(5)

for i in range(0,5):
    turtle.color(random.choice(["red","yellow","blue","green","orange"]))
    turtle.forward(100)
    turtle.right(144)

turtle.exitonclick()
