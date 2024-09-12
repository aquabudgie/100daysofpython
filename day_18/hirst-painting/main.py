import colorgram as col
import turtle as t
from random import choice


timmy = t.Turtle()
timmy.hideturtle()
timmy.speed(0)

t.colormode(255)
colours = col.extract("hirstspotpainting.jpg", 30)
colour_tuples = []
for colour in colours:
    colour_tuple = (colour.rgb.r, colour.rgb.g, colour.rgb.b)
    colour_tuples.append(colour_tuple)

for _ in range(6):
    colour_tuples.pop(0)


def random_colour(colour_list):
    rgb = choice(colour_list)
    return rgb


# paint a painting with 10x10 spots
# each dot around 20 in size, spaced by about 50


def dotted_line(size, number, skip):
    for _ in range(number):
        timmy.dot(size, random_colour(colour_tuples))
        timmy.teleport(timmy.pos()[0] + skip)


def jump_up_line(y):
    timmy.teleport(-225, timmy.pos()[1] + y)


timmy.teleport(-225, -225)
for _ in range(10):
    dotted_line(20, 10, 50)
    jump_up_line(50)

screen = t.Screen()
screen.exitonclick()
