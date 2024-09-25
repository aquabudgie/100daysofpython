from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.teleport(350, 0)
        self.speed(0)
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white", "white")

    def paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)