import turtle
import random
from typing import Text
wn = turtle.Screen()

wn.bgcolor("black")
wn.setup(width=1000, height=900)
turtle.color("white")

one = turtle.Turtle()
two = turtle.Turtle()
three = turtle.Turtle()
four = turtle.Turtle()
five = turtle.Turtle()
six = turtle.Turtle()

one_end = turtle.Turtle()
two_end = turtle.Turtle()
three_end = turtle.Turtle()
four_end = turtle.Turtle()
five_end = turtle.Turtle()
six_end = turtle.Turtle()

one_end.color("white")
two_end.color("white")
three_end.color("white")
four_end.color("white")
five_end.color("white")
six_end.color("white")

end_x=400
end_y=250

one_end.penup()
two_end.penup()
three_end.penup()
four_end.penup()
five_end.penup()
six_end.penup()

one_end.goto(end_x, end_y)
two_end.goto(end_x, end_y-100)
three_end.goto(end_x, end_y-200)
four_end.goto(end_x, end_y-300)
five_end.goto(end_x, end_y-400)
six_end.goto(end_x, end_y-500)

one_end.pendown()
two_end.pendown()
three_end.pendown()
four_end.pendown()
five_end.pendown()
six_end.pendown()

x=-390
y=250

one.speed(10)
two.speed(10)
three.speed(10)
four.speed(10)
five.speed(10)
six.speed(10)

one.color("blue")
two.color("red")
three.color("green")
four.color("yellow")
five.color("orange")
six.color("purple")

one.penup()
two.penup()
three.penup()
four.penup()
five.penup()
six.penup()

one.shape("turtle")
two.shape("turtle")
three.shape("turtle")
four.shape("turtle")
five.shape("turtle")
six.shape("turtle")

one.goto(x, y)
two.goto(x, y-100)
three.goto(x, y-200)
four.goto(x, y-300)
five.goto(x, y-400)
six.goto(x, y-500)

one.pendown()
two.pendown()
three.pendown()
four.pendown()
five.pendown()
six.pendown()



for a in range(500):
    one.speed(10)
    two.speed(10)
    three.speed(10)
    four.speed(10)
    five.speed(10)
    six.speed(10)
    one.forward(random.randint(1, 100))
    two.forward(random.randint(1, 100))
    three.forward(random.randint(1, 100))
    four.forward(random.randint(1, 100))
    five.forward(random.randint(1, 100))
    six.forward(random.randint(1, 100))
    turtle.color("white")
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, -500)
    if one.xcor==400:
        turtle.write("blue won")
    elif two.xcor==400:
        turtle.write("red won")
    elif three.xcor==400:
        turtle.write("green won")
    elif four.xcor==400:
        turtle.write("yellow won")
    elif five.xcor==400:
        turtle.write("orange won")

turtle.mainloop()