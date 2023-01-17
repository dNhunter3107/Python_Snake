from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.h_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.maintain_score()
        self.hideturtle()

    def maintain_score(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.h_score}", align="center", font=("Arial", 24, "normal"))

    def reset_progress(self):
        if self.score > self.h_score:
            self.h_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.h_score}")
        self.score = 0
        self.maintain_score()

    '''def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=("Arial", 24, "normal"))'''

    def increase_score(self):
        self.score += 1
        self.maintain_score()
