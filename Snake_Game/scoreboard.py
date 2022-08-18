from turtle import Turtle


class Scoreboard(Turtle):
    """Keeping track of score by a created turtle at the top of the screen"""
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        """Recording the score after any consumption is made"""
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align="center", font=("Courier", 20, "normal"))

    def high_score_checker(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
            self.score = 0
        else:
            self.score = 0
        self.update_scoreboard()

    def increase_the_score(self):
        """Increment of the score after any collision with the food"""
        self.score += 1
        self.update_scoreboard()
