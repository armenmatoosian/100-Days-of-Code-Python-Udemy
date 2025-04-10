from turtle import Turtle
from turtle import Screen
import pandas as pd
from pandas import DataFrame

class GuessesAndAnswers:
    def __init__(self):
        self.t = Turtle()
        self.screen = Screen()
        self.df = DataFrame()
        self.t.hideturtle()
        self.states_info_df = pd.DataFrame(pd.read_csv("50_states.csv"))
        self.state_name_list = self.states_info_df["state"]
        print(self.state_name_list)
        self.state_answer = ""
        self.answer_list = []
        self.score = 0

    def guess_answer(self):
        self.state_answer = self.screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

    def check_answer(self):
        for state in self.state_name_list:
            if self.state_answer == state:
                self.answer_list.append(self.state_answer)
                self.score += 1
                return True
            elif self.state_answer != state:
                return False

    def score(self):
        score_tracker = self.score
        self.state_answer = self.screen.textinput(title=f"{score_tracker}/50 States Correct", prompt="What's another state's name?").title()