x = 0
y = 0


def move():
    x + 1


def turn_left():
    x + 1


def wall_in_front():
    return


def wall_on_right():
    return


def at_goal():
    return


def front_is_clear():
    return


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def go_over_top():
    turn_right()
    move()
    turn_right()


def hurdle():
    turn_left()
    while wall_on_right():
        move()
    go_over_top()
    while not wall_in_front():
        move()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    else:
        hurdle()
