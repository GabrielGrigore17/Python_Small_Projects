from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def refresh(self):
        self.score += 1
        self.clear()
        self.write("Score: {}".format(self.score), move=False, align="center", font=("Arial", 16, "normal"))
