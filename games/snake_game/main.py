from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

SPEED = 0.1
CRI = 300
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(SPEED)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent()
        score.score_inc()
        score.refresh()

    if snake.head.xcor() > CRI or snake.head.xcor() < -CRI or snake.head.ycor() > CRI or snake.head.ycor() < -CRI:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
