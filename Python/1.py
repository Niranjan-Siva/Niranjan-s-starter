import turtle
import time

win=turtle.Screen()
win.bgcolor("black")
win.title("Circle")
n=turtle.Turtle()
n.hideturtle()
n.speed(10)
n.width(2)
n.color("#3d5dff")
px1=.05
n.penup()
n.goto(0, -200)
n.pendown()
while True:
    n.forward(px1)
    n.left(.1)
    n.forward(px1)
