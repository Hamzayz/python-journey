from turtle import Turtle
import os

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color("white")  # Changed to yellow for better visibility
        self.penup()
        self.goto(0, 200)  # Position at top of screen
        self.hideturtle()
        self.update_scoreboard()

    def get_high_score(self):
        try:
            file_path = os.path.join(os.path.dirname(__file__), "data.txt")
            with open(file_path, "r") as data:
                content = data.read().strip()
                return int(content) if content else 0
        except (FileNotFoundError, ValueError):
            return 0

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            try:
                file_path = os.path.join(os.path.dirname(__file__), "data.txt")
                with open(file_path, "w") as data:
                    data.write(str(self.high_score))
            except Exception as e:
                print(f"Error saving high score: {e}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()