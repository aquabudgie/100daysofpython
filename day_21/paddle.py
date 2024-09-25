from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position.lower()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white", "white")
        if self.position == "right":
            self.teleport(350, 0)
        else:
            self.teleport(-350, 0)

    def paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)