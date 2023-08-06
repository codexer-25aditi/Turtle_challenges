from turtle import Turtle,Screen
import random

timmy=Turtle()
screen=Screen()
timmy.shape("circle")
timmy.color("red")
colours=["royal blue","green yellow","gold","deep pink","violet"]
directions=[0,90,180,270]
timmy.pensize(15)
timmy.speed("fastest")
for i in range(25):
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

    timmy.color(random.choice(colours))

screen.exitonclick()
