from turtle import Turtle, Screen

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.move_speed = 15  # Reduced speed for smoother movement

    def go_up(self):
        if self.ycor() < 280:  # Prevent paddle from going above screen
            new_y = self.ycor() + self.move_speed
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -280:  # Prevent paddle from going below screen
            new_y = self.ycor() - self.move_speed
            self.goto(self.xcor(), new_y)
