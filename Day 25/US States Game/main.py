# my code for U.S. States Game Part 2: Challenge with .csv
import turtle
import pandas as pd
from guesses_answers import GuessesAndAnswers

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(.25, .3)
turtle.shape(image)

guesses_and_answers = GuessesAndAnswers()

game_is_on = True

while game_is_on:
    guesses_and_answers.guess_answer()
    if guesses_and_answers.state_answer == "Exit": # my code for U.S. States Game Part 3: Saving Data to .csv, adapted from solution code
        guesses_and_answers.save_missing_states() # my code for U.S. States Game Part 3: Saving Data to .csv, adapted from solution code
        break # my code for U.S. States Game Part 3: Saving Data to .csv, adapted from solution code
    guesses_and_answers.check_answer()

# my code for U.S. States Game Part 3: Saving Data to .csv
# if game_is_on is False:


# code from US States Game Part 1: Setup -- not needed, just to show how to get coordinates by clicking on screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()