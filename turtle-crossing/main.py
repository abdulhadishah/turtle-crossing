import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#212121")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.car_moves()

    if player.at_finish_line():
        car_manager.level_up()
        score_board.level_up()
        player.level_up()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()