from turtle import Turtle
DOWN_RIGHT = 1
DOWN_LEFT = 2
UP_RIGHT = 3
UP_LEFT = 4
DISTANCE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.extra_speed = 0
        self.direction = UP_RIGHT

    def move(self):
        self.wall_collision()
        if self.direction is UP_RIGHT:
            self.goto(self.xcor() + DISTANCE + self.extra_speed, self.ycor() + DISTANCE + self.extra_speed)
        elif self.direction is UP_LEFT:
            self.goto(self.xcor() - DISTANCE - self.extra_speed, self.ycor() + DISTANCE + self.extra_speed)
        elif self.direction is DOWN_RIGHT:
            self.goto(self.xcor() + DISTANCE + self.extra_speed, self.ycor() - DISTANCE - self.extra_speed)
        elif self.direction is DOWN_LEFT:
            self.goto(self.xcor() - DISTANCE - self.extra_speed, self.ycor() - DISTANCE - self.extra_speed)

    def wall_collision(self):
        if self.ycor() > 270 or self.ycor() < -270:
            if self.direction is UP_LEFT:
                self.direction = DOWN_LEFT
            elif self.direction is UP_RIGHT:
                self.direction = DOWN_RIGHT
            elif self.direction is DOWN_LEFT:
                self.direction = UP_LEFT
            elif self.direction is DOWN_RIGHT:
                self.direction = UP_RIGHT

    def paddle_collision(self, other):
        if self.distance(other) < 30:
            if self.direction is UP_LEFT:
                self.direction = UP_RIGHT
            elif self.direction is UP_RIGHT:
                self.direction = UP_LEFT
            elif self.direction is DOWN_LEFT:
                self.direction = DOWN_RIGHT
            elif self.direction is DOWN_RIGHT:
                self.direction = DOWN_LEFT
            return True
        return False

    def return_to_start(self):
        if self.xcor() > 500:
            self.goto(0, 0)
            self.direction = UP_LEFT
        if self.xcor() < -500:
            self.goto(0, 0)
            self.direction = UP_RIGHT

    def is_out_of_bounds(self):
        if self.xcor() > 500:
            return True
        if self.xcor() < -500:
            return True
        return False
