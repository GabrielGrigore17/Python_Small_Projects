from turtle import Turtle


class OnScreenText(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_on_screen(self, x, y, name):
        self.goto(x, y)
        self.write(name, align="center")
