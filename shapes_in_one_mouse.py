from turtle import Turtle,Screen
import random

timmy=Turtle()
screen=Screen()
timmy.shape("circle")
timmy.color("red")
colours=["royal blue","green yellow","gold","deep pink","violet"]
for i in range(3,10):
    angle=360/i
    timmy.color(random.choice(colours))
    for j in range(i+1):

        timmy.forward(100)
        timmy.right(angle)

screen.exitonclick()
