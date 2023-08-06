import turtle
from turtle import Turtle,Screen
import random

timmy=Turtle()
screen=Screen()
timmy.shape("circle")
timmy.color("red")
turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colors=(r,g,b)
    return colors

directions=[0,90,180,270]
timmy.pensize(15)
timmy.speed("fastest")
for i in range(25):
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

    timmy.color(random.choice(random_color()))

screen.exitonclick()
