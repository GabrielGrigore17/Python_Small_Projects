import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")
screen.title("Turtle Crossing")

cars = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.respawn()
    cars.move_cars()

    for car in cars.cars:
        if player.is_collision(car):
            scoreboard.game_over()
            game_is_on = False

    if player.win_level():
        scoreboard.level += 1
        scoreboard.update()
        cars.increase_speed()
        player.respawn()

screen.exitonclick()
