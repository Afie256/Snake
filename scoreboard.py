from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.player_score}", False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.clear()
        self.player_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align=ALIGNMENT, font=FONT)
