# my code for U.S. States Game Part 2: Challenge with .csv
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
        self.state_name_list = self.states_info_df["state"].to_list()
        self.state_answer = ""
        self.answer_list = []
        self.score = 0

    def guess_answer(self):
        if self.score == 0:
            self.state_answer = self.screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
        elif self.score > 0:
            self.state_answer = self.screen.textinput(title=f"{self.score}/50 States Correct", prompt="What's another state's name?").title()
        elif self.score == 50:
            self.t.write("You won! You listed all 50 states!", True, "center", ("Arial", 16, "normal"))

    def check_answer(self):
        for state in self.state_name_list:
            if state == self.state_answer:
                self.write_state(state)
                self.answer_list.append(self.state_answer)
                self.add_score()
                return True

    def add_score(self):
        self.score += 1

    def write_state(self, state_name):
        writer = Turtle()
        writer.hideturtle()
        writer.penup()
        state_data = self.states_info_df[self.states_info_df.state == state_name]
        x = int(state_data.x)
        y = int(state_data.y)
        writer.goto(x, y)
        writer.write(state_name, align="center", font=("Arial", 8, "normal"))

    # my code for U.S. States Game Part 3: Saving Data to .csv, adapted from solution code
    def save_missing_states(self):
        missing_states = []
        for state in self.state_name_list:
            if state not in self.answer_list:
                missing_states.append(state)
        missing_states_df = pd.DataFrame(missing_states)
        missing_states_df.to_csv("states_to_learn.csv")

    # # my code for U.S. States Game Part 3: Saving Data to .csv, with help from Claude - could not get it to work
    # def save_missing_states(self):
    #     missing_states = [state for state in self.state_name_list if state not in self.answer_list]
    #     missing_states_df = pd.DataFrame(missing_states, columns=['state'])
    #     missing_states_df.to_csv()