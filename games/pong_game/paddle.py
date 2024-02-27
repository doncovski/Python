from turtle import Turtle

MOVE_DIST = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5.0, 1.0, 1)
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.goto(position)


    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DIST)

    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_DIST)
