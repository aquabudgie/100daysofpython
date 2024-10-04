from turtle import Screen
from time import sleep
from paddle import Paddle
from ball import Ball


screen = Screen()
screen_height = 600
screen_width = 800
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.title(titlestring="Pong Game")
screen.tracer(0) # stop screen animation

right_paddle = Paddle("right")
left_paddle = Paddle("left")

ball = Ball()

screen.listen()
screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")
screen.onkey(left_paddle.paddle_up, "w")
screen.onkey(left_paddle.paddle_down, "s")



game_on = True

while game_on:
    sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()