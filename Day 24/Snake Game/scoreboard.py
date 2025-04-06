# # my code for Snake Game Part 2: Create a Scoreboard
# # my code works just as well as the solution code, but it's easier to complete the following challenges with solution code
# from turtle import Turtle
#
# class Scoreboard(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         self.score = 0
#
#     def scoreboard(self):
#         self.penup()
#         self.ht()
#         self.pencolor("white")
#         self.speed("fastest")
#         self.goto(0, 280)
#         self.write(arg=f"Score: {self.score}", move=False, align="center", font=('Arial', 12, 'normal'))
#
#     def score_refresh(self):
#         self.clear()
#         self.score += 1
#         self.scoreboard()

# solution code for Snake Game Part 2: Create a Scoreboard
from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.data = open("data.txt", mode="r+").read() # Read and Write High Score to a File
        self.high_score = int(self.data) #code from Day 24: Add a High Score to the Snake Game, and Read and Write High Score to a File
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT) # code from Day 24: Add a High Score to the Snake Game

    # code from Day 24: Add a High Score to the Snake Game
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data: # Read and Write High Score to a File
                data.write(f"{self.high_score}") # Read and Write High Score to a File
        self.score = 0

    # # code from Day 24: Add a High Score to the Snake Game
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        # self.clear() # code from Day 24: Add a High Score to the Snake Game
        self.update_scoreboard()