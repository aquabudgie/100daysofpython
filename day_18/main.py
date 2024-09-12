# from turtle import Turtle, Screen
import turtle as t
from random import randint, randrange


timmy = t.Turtle()

timmy.shape("turtle")
timmy.color("darkseagreen4")
timmy.speed(0)
t.colormode(255)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)


def square_right():
    timmy_go = True
    while timmy_go:
        timmy.forward(100)
        timmy.right(90)
        if abs(timmy.pos()) < 1:
            timmy_go = False


def dashed_line(length):
    for _ in range(length):
        timmy.forward(10)
        timmy.teleport(timmy.pos()[0] + 10)
    return


def dashed_line2(length):
    for _ in range(length):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()
    return


def polygons():
    sides = range(3, 11)
    for number in sides:
        random_colour()
        draw_polygon(number)


def random_colour():
    timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))


def draw_polygon(num_sides):
    degrees = 360
    angle = degrees / num_sides
    for _ in range(num_sides):
        dashed_line2(5)
        timmy.right(angle)


def random_direction():
    direction = randrange(0, 360, 90)
    print(direction)
    timmy.setheading(direction)
    return


def stop():
    return False


def random_walk():
    timmy.width(10)
    timmy.speed(10)
    for _ in range(200):
        random_direction()
        random_colour()
        timmy.forward(40)


def spirograph(size_of_gap):
    timmy.hideturtle()
    angle = size_of_gap
    for i in range(int(360 / angle)):
        random_colour()
        timmy.circle(100)
        timmy.setheading(timmy.heading() + angle)


screen = t.Screen()
screen.screensize(1000, 1000)
# random_walk()
spirograph(6)
screen.exitonclick()
