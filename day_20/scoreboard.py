from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setpos(0, 280)
        self.color("white")
        self.score = 0
        self.font= "Courier"
        self.fontsize = 16
        self.fontstyle = "bold"
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align = "center", font=(self.font, self.fontsize, self.fontstyle))

    def add_score(self):
        self.score += 1
        
    def game_over(self):
        self.clear()
        self.write(f"GAME OVER. Your final score was: {self.score}", align = "center", font=(self.font, self.fontsize, self.fontstyle))

