from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle("right")
l_paddle = Paddle("left")
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()
    for segment in r_paddle.segments:
        if ball.paddle_collision(segment):
            ball.extra_speed += 1
            break
    for segment in l_paddle.segments:
        if ball.paddle_collision(segment):
            ball.extra_speed += 1
            break

    if ball.is_out_of_bounds():
        ball.extra_speed = 0
        if ball.xcor() < 0:
            scoreboard.r_score += 1
        else:
            scoreboard.l_score += 1
        ball.return_to_start()

    scoreboard.update()


screen.exitonclick()
