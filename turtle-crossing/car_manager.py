import random
from turtle import Turtle

COLORS = [
    "#FF5252",  # vivid red
    "#FF7043",  # orange
    "#FFB74D",  # warm amber
    "#FFD600",  # bright yellow
    "#AEEA00",  # lime
    "#69F0AE",  # mint green
    "#00E676",  # bright green
    "#40C4FF",  # sky blue
    "#2979FF",  # strong blue
    "#7E57C2",  # purple
    "#EC407A",  # pink
    "#F06292",  # soft pink
    "#26C6DA",  # cyan
    "#8D6E63",  # mocha/brown
    "#BDBDBD"   # silver/gray
]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            x_axis = random.randint(280, 350)
            y_axis = random.randint(-250, 250)
            new_car.goto(x_axis, y_axis)
            self.all_cars.append(new_car)

    def car_moves(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT