import turtle as t
from random import randint

screen = t.Screen()
screen_height = 500
screen_width = 800
race_finish = screen_width / 2 - 40
screen.setup(width=screen_width, height=screen_height)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a colour:"
)
print(user_bet)

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_height = screen_height / 2
turtle_interval = screen_height / (len(colours) + 1)
turtles = {}
for colour in colours:
    turtle_height -= turtle_interval
    turtles[colour] = t.Turtle(shape="turtle")
    turtles[colour].color(colour)
    turtles[colour].penup()
    # timmy.teleport(-300, 0)
    turtles[colour].goto(-380, turtle_height)

finish_line = t.Turtle(visible=False)
finish_line.teleport(race_finish, screen_height / 2)
finish_line.color("black")
finish_line.setheading(270)


def dashed_line(length):
    for _ in range(length):
        finish_line.forward(10)
        finish_line.teleport(race_finish, finish_line.pos()[1] - 10)
    return


dashed_line(int(screen_height / 10))

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtles[turtle].forward(randint(0, 10))
        if turtles[turtle].xcor() >= race_finish:
            is_race_on = False
            print(f"The winner is {turtle}")
            if user_bet == turtle:
                print("You win!")
            else:
                print("You lose!")
            break


screen.exitonclick()
