import turtle
import math
import random

turtle.Screen().bgcolor("blue")

turtle.hideturtle()
turtle.speed(10)
n = 900
def ellipse(X,Y,a,b,ts,te,P):
    t = ts
    for i in range(n):
        x = a*math.cos(t)
        y = b*math.sin(t)
        P.append((x+X,y+Y))
        t += (te-ts)/(n-1)


def dist(p1,p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5


def draw_arc(p1,p2,ext):
    turtle.up()
    turtle.goto(p1)
    turtle.seth(turtle.towards(p2))
    a = turtle.heading() 
    b = 360-ext 
    c = (180-b)/2
    d = a-c
    e = d-90
    r = dist(p1,p2)/2/math.sin(math.radians(b/2))
    turtle.seth(e)
    turtle.down()
    turtle.circle(r,ext,100)
    return (turtle.xcor(),turtle.ycor()) 


def cloud(P):
    step = n//10 
    a = 0 
    b = a + random.randint(step//2,step*2) 
    p1 = P[a]
    p2 = P[b]
    turtle.fillcolor('#707070')
    turtle.begin_fill()
    p3 = draw_arc(p1,p2,random.uniform(70,180))
    while b < len(P)-1:
        p1 = p3 
        if b < len(P)/2:
            ext = random.uniform(70,180)
            b += random.randint(step//2,step*2)
        else:
            ext = random.uniform(30,70)
            b += random.randint(step,step*2)
        b = min(b,len(P)-1) 
        p2 = P[b]
        p3 = draw_arc(p1,p2,ext)
    turtle.end_fill()

P = [] # starting from empty list
ellipse(0,0,300,200,0,math.pi,P) # taller top half
ellipse(0,0,300,50,math.pi,math.pi*2,P) # shorter bottom half
cloud(P)
turtle.done()