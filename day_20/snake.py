from turtle import Turtle, mode


starting_positions = [(0,0), (-20,0), (-40,0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.move_distance = 22
        mode("standard")
        for i in range(3):
            self.add_segment(starting_positions[i])
        self.head = self.segments[0]

    def add_segment(self, position=None):
        segment = Turtle(shape="square")
        segment.penup()
        segment.color("white")
        if position:
            segment.setpos(position)
        else: 
            segment.setpos(self.segments[-1].pos())
        self.segments.append(segment)
        
    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].goto(self.segments[i-1].pos())
        self.head.forward(self.move_distance)
    
    def up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)

    def down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)

    def left(self):
        if not self.head.heading()  == 0:
            self.head.setheading(180)

    def right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)