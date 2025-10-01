import sys
import os
sys.dont_write_bytecode = True
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

# Day 20
# project create snake game:
# 1) Create snake

from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

Turtle().speed("slow")
screen = Screen()
screen.setup(width=600, height=500)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()  # Create an instance of Snake
food = Food()    # Create an instance of Food
scoreboard = Scoreboard()  # Create an instance of Scoreboard

# 3) Control the snake
# Add keyboard controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # 4)Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()  # This should now work
        snake.extend()

        # 5) Create the scoreboard
        scoreboard.increase_score()

# 6) Detect the collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
        scoreboard.reset()
        snake.reset()
        
# 7) Detect the collision with tail

    for segments in snake.snakes[1:]:
        if snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()