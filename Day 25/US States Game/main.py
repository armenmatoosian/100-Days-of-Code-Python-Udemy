import turtle
import pandas as pd
from guesses_answers import GuessesAndAnswers

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(.25, .3)
turtle.shape(image)

# answer_state = input("Guess a state: ").title()
# print(answer_state)

guesses_and_answers = GuessesAndAnswers()

game_is_on = True

while game_is_on:
    guesses_and_answers.guess_answer()
    guesses_and_answers.check_answer()
    if guesses_and_answers.check_answer() is True:
        game_is_on = True
        guesses_and_answers.score()
    elif guesses_and_answers.check_answer() is False:
        game_is_on = False
    print(game_is_on)








# code from US States Game Part 1: Setup -- not needed, just to show how to get coordinates by clicking on screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()