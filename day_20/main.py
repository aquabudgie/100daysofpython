from time import sleep
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen_height = 640
screen_width = 640
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.title(titlestring="Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_over = False

while not game_over:
    sleep(0.10)
    snake.move()

    # Detect collision between snake and food
    if snake.head.distance(food) <= 15:
        # print("nom nom nom")
        snake.add_segment()
        food.hideturtle()
        food = Food()
        scoreboard.add_score()
        scoreboard.write_score()

    # Detect collision between snake and snake
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <= 10:
            snake.head.color("red")
            segment.color("red")
            game_over = True

    # Detect collision between snake and wall
    if abs(max(snake.head.pos(), key=abs)) >= 300:
        snake.head.color("red")
        game_over = True

    screen.update()

scoreboard.game_over()

screen.exitonclick()