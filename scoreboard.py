from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.speed ("fastest")
        self.penup()
        self.goto(0, 260)
        self.write(f"score : {self.score}", align="center", font=("Arial", 20, "bold"))
        self.hideturtle()

    def game_over(self):
        self.hideturtle()
        self.color("white")
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"score : {self.score}", align="center", font=("Arial", 20, "bold"))

