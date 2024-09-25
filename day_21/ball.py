from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        # self.speed(0)
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.color("white", "white")
        self.setpos(0,0)
        self.seth(38)

    def move(self):
        self.forward(10)