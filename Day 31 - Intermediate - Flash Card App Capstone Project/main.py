from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
random_english_word = ""
random_word = {}
words_to_learn = {}

# my code for Step 2 - Create New Flash Cards, made some changes based on solution video otherwise mostly the same
# ----------------------------------------- WORD RANDOMIZER ----------------------------------------- #
def random_word_generator():
    global random_english_word, flip_timer, random_word, words_to_learn
    window.after_cancel(flip_timer) # from solution video for Step 3
    # while watching solution video, realized line below is not needed because pandas opens the file
    # with open(file="data/french_words.csv") as file:

    # my code for Step 4 - Save Your Progress, checking for words_to_learn.csv; on the right tack but in the wrong location
    try:
        words_to_learn = pd.read_csv("data/words_to_learn.csv").to_dict(orient="records")
    except FileNotFoundError:
        words_to_learn = pd.read_csv("data/french_words.csv").to_dict(orient="records")

    random_word = random.choice(words_to_learn)
    random_french_word = random_word["French"]
    random_english_word = random_word["English"]
    canvas.itemconfig(card_title, text="French", fill="black") # added this while watching solution video
    canvas.itemconfig(card_word, text=f"{random_french_word}", fill="black") # modified this while watching solution video
    canvas.itemconfig(card, image=card_front_img) # was missing this, got from solution video for Step 3
    flip_timer = window.after(3000, func=card_flipper) # from solution video for Step 3

# my code mixed with solution code for Step 3 - Flip the Cards!, was not able to figure out .after() due to args error
# ----------------------------------------- CARD FLIPPER ----------------------------------------- #
def card_flipper():
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_english_word, fill="white")

# ----------------------------------------- SAVING PROGRESS ----------------------------------------- #
# solution code for Step 4 - Save Your Progress
def is_known():
    words_to_learn.remove(random_word)
    print(len())
    data = pd.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv")

# # my code for Step 4 - Save Your Progress, was not able to remove learned words
# def remove_learned_word():
#     global words_to_learn, random_english_word
#     words_to_learn.remove([random_english_word])


# my code for Step 1 - Create the User Interface (UI) with Tkinter, same as solution
# ----------------------------------------- UI SETUP ----------------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50 ,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=card_flipper) # from solution video for Step 3

# canvas with cards
canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 300, image=card_front_img)
# card_back = canvas.create_image(400, 300, image=card_back_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text=f"", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# right button
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known) # from Step 4 solution video
right_button.grid(row=1, column=1)

# wrong button
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=random_word_generator)
wrong_button.grid(row=1, column=0)

# added this based on solution vide for Step 2
random_word_generator()

window.mainloop()