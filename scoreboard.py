from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

# TODO: 5. Create a scoreboard
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.write_score()


    def write_score(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    

    def increase_score(self):
        self.score+=1
        self.clear()
        self.write_score()