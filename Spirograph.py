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


timmy.speed("fastest")
def drawSpirograph(size):
    for _ in range(int(360/size)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+size)

drawSpirograph(5)

screen.exitonclick()
