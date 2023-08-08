from turtle import Turtle
Data = "Intermediate/Day 24(Snake Game Improved)/Snake_Improved/data.txt"

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        with open(Data) as file:
            self.high_score = int(file.read())
 
        self.setup()

    def setup(self):
        self.clear()
        self.goto(0, 270)
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
    
    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(Data, "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    

