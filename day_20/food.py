from turtle import Turtle
from random import randint, randrange


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("seagreen4")
        self.speed(0)
        self.heading = randrange(0, 360, 90)
        random_x = self.my_round(randint(-270, 270))
        random_y = self.my_round(randint(-270, 270))
        self.teleport(random_x, random_y)

    def my_round(self, number):
        base = 30
        rounded = base * round(number/base)
        # print(rounded)
        return rounded

