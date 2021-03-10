from turtle import Turtle
STARTING_POSITIONS_RIGHT = [(350, -40), (350, -20), (350, 0), (350, 20), (350, 40)]
STARTING_POSITIONS_LEFT = [(-350, -40), (-350, -20), (-350, 0), (-350, 20), (-350, 40)]
MOVE_DISTANCE = 20


class Paddle:
    def __init__(self, side=str):
        self.side = side
        self.segments = []
        self.create_paddle()

    def create_paddle(self):
        if self.side is "left":
            positions = STARTING_POSITIONS_LEFT
        else:
            positions = STARTING_POSITIONS_RIGHT
        for position in positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move_up(self):
        if self.segments[-1].ycor() < 280:
            for segment in self.segments:
                segment.goto(segment.xcor(), segment.ycor() + MOVE_DISTANCE)

    def move_down(self):
        if self.segments[0].ycor() > -280:
            for segment in self.segments:
                segment.goto(segment.xcor(), segment.ycor() - MOVE_DISTANCE)
