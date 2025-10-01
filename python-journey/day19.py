# Day :19
# More Turtle Graphics, Event Listners, State and Multiplication Instances:

from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -50, 0, 50, 100, 150]

def create_turtles():
    all_turtles = []
    for index in range(6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colours[index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_positions[index])
        all_turtles.append(new_turtle)
    return all_turtles

turtles = create_turtles()

if user_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You win! The {winning_turtle} turtle is the winner.")
            else:
                print(f"You lost! The {winning_turtle} turtle is the winner.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
