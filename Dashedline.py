from turtle import Turtle,Screen

timmy=Turtle()
screen=Screen()
timmy.shape("circle")
timmy.color("red")
for i in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
screen.exitonclick()
