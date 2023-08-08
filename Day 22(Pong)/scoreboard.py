from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.rewrite()
        
    def rewrite(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
    
    def l_point(self):
        self.clear()
        self.l_score += 1
        self.rewrite()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.rewrite()