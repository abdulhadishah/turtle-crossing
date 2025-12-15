from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("#FFFFFF")
        self.penup()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.goto(-220, 260)
        self.clear()
        self.write(f"Level: {self.level}", True, "center", FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", True, "center", FONT)