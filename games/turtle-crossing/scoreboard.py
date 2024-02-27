from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.goto(-220, 260)
        self.score = 1
        self.refresh()

    def score_inc(self):
        self.score +=1
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align=ALIGN, font=FONT)

    def refresh(self):
        self.clear()
        self.write(f"Level: {self.score}", False, align=ALIGN, font=FONT)
