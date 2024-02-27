import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? (red, orange, yellow, green, blue, purple)").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
is_race_on = False

for tur in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[tur])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=-130+tur*50)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost! The {winning_color} is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
