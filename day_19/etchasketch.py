import turtle as t

# from utils import move_forwards

timmy = t.Turtle()


# move_forwards(timmy)
def move_forwards():
    timmy.forward(10)


def turn_right():
    timmy.right(12)


def turn_left():
    timmy.left(12)


def move_backwards():
    timmy.back(10)


def clear():
    timmy.penup()
    timmy.clear()
    timmy.home()
    timmy.pendown()


def exit():
    screen.bye()


screen = t.Screen()
screen.setup(width=0.8, height=0.8)
screen.textinput(title="Make your bet", prompt="")


screen.listen()


screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.onkey(key="x", fun=exit)
# screen.mainloop()
screen.exitonclick()
