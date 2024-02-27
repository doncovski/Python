from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 16, 'normal')
FONT_OVER = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.speed("fastest")
        self.score = 0
        with open("data.txt") as f:
            self.high_score = int(f.read())
        self.refresh()

    def score_inc(self):
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
            self.high_score = self.score
        self.score = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", False, align=ALIGN, font=FONT)
