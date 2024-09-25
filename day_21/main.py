from turtle import Screen


screen = Screen()
screen_height = 600
screen_width = 800
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.title(titlestring="Pong Game")
screen.exitonclick()