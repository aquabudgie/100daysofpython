from turtle import Screen
from paddle import Paddle


screen = Screen()
screen_height = 600
screen_width = 800
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.title(titlestring="Pong Game")
screen.tracer(0) # stop screen animation

paddle = Paddle()

screen.listen()
screen.onkey(paddle.paddle_up, "Up")
screen.onkey(paddle.paddle_down, "Down")



game_on = True

while game_on:
    screen.update()

screen.exitonclick()