import turtle
from turtle import Turtle, Screen
import random

# for i in range(3,12):
#     tim = Turtle()
#     tim.color(colors[random.choice(colors)])
#     for _ in range(i):
#         tim.forward(100)
#         tim.right(360 / i)

direction = [0,90,180,270]

tim = Turtle()
turtle.colormode(255)

def rand_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b

tim.pensize(1)
tim.speed("fastest")


def draw_cirle(size):
    for i in range(int(360/size)):
        tup = rand_color()
        tim.pencolor(tup)
        tim.circle(150)
        tim.setheading(tim.heading() + size)

draw_cirle(6)
screen = Screen()
screen.exitonclick()
