x = 0


def move():
    x + 1


def turn_left():
    x + 1


def front_is_clear():
    return


def right_is_clear():
    return


def at_goal():
    return


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    return


def escape_right_loop():
    if front_is_clear():
        move()
        return
    else:
        turn_left()
        escape_right_loop()


right_count = 0
while not at_goal():
    if right_is_clear():
        right_count += 1
        if right_count >= 4:
            escape_right_loop()
        else:
            turn_right()
            move()
    elif front_is_clear():
        move()
        right_count = 0
    else:
        turn_left()
        right_count = 0
