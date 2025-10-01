from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# turtle which will move
class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)  # Make turtle face upward

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_start(self):
        self.goto(STARTING_POSITION)

    def at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False
        



    
