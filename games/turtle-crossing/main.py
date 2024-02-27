import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
player1 = Player()
score = Scoreboard()
screen.listen()
screen.onkey(fun=player1.move, key="Up")
car_manager = CarManager()
game_is_on = True
i = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    for car in car_manager.all_cars:
        if player1.distance(car) < 20:
            game_is_on = False
            score.game_over()
    if player1.finish_line():
        score.score_inc()
        car_manager.inc_speed()

screen.exitonclick()
