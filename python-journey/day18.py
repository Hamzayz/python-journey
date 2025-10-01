# Turtle Graphics, Turples and Importing Modules:
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("orange1")
tim.speed("fastest")
tim.shapesize(1)
tim.pensize(1)
tim.colormode(255)

def colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_g_b = (r, g, b)
    return r_g_b

def circle(space):
    for circle in range(int(360/space)):
        tim.circle(100)
        tim.penup()
        tim.right(space)
        tim.forward(2)
        tim.pendown()
        tim.color(colour())

circle(5)

screen = Screen()
screen.exitonclick()

# Import modules basic:

from turtle import * # "*" means everything

# Aliases:
import turtle as T 
tim=T.turtles()

# making shapes:




