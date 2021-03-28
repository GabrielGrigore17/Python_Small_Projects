from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
NO_CARS = 25
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2
STARTING_X_COR = 330


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.spawn_cars()

    def spawn_cars(self):
        for i in range(NO_CARS):
            car = Turtle()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.shape("square")
            car.penup()
            y = random.randrange(-240, 240, 10)
            x = random.randrange(-300, 300, 20)
            car.goto(x, y)
            self.cars.append(car)

    def respawn(self):
        for car in self.cars:
            if car.xcor() < -330:
                y = random.randrange(-240, 240, 10)
                car.goto(STARTING_X_COR, y)

    def move_cars(self):
        for car in self.cars:
            car.goto(car.xcor() - self.speed, car.ycor())

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
