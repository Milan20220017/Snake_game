from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier",24,"normal")


def ucitaj_iz_datoteke():
    # C:\Users\s\PycharmProjects\day\snake - game
    with open("../../../OneDrive/Radna površina/high_score.txt") as file:
        najveci_rezultat=int(file.read())
    return najveci_rezultat


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.broj=0
        self.high_score=ucitaj_iz_datoteke()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.broj} High score: {self.high_score}", False, align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.broj>self.high_score:
            self.high_score=self.broj
            with open("../../../OneDrive/Radna površina/high_score.txt",mode="w") as file:
                file.write(f"{self.high_score}")

        self.broj=0
        self.update_scoreboard()
    def povecaj(self):
        self.broj+=1
        self.update_scoreboard()
