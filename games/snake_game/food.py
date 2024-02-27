from turtle import Turtle
import random

FOOD_COLOR = "red"
FOOD_SHAPE = "circle"


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(FOOD_COLOR)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-260, 260), random.randint(-260, 260))
