from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("#00E676")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        y_goto = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y_goto)

    def at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return  True
        else:
            return False

    def level_up(self):
        self.goto(STARTING_POSITION)
