from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(width=300, height=400, padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", font=("Arial", 15, "bold"), bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Quizzler", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        # I had adding padding to x and y in the buttons and label, but pady=50 here is all you need
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png") # I originally had self, but it does not need self since it won't be used anywhere else
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file="images/false.png") # I originally had self, but it does not need self since it won't be used anywhere else
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_answer)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        # solution code for Give Feedback to the Player, Keep Score and Fix the Bugs =)
        self.canvas.config(bg="white")
        # code for Give Feedback to the Player, Keep Score and Fix the Bugs =)
        if self.quiz.still_has_questions():
            # code for Give Feedback to the Player, Keep Score and Fix the Bugs =)
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    # same as true pressed in solution
    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    # same as false pressed in solution
    def false_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    # my code for Give Feedback to the Player, Keep Score and Fix the Bugs =)
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        elif is_right is False:
            self.canvas.config(bg="red")
        """
        solution code for Give Feedback to the Player, Keep Score and Fix the Bugs =)
        --------------------
        I had tried calling self.get_next_question when attempting to solve the problem. I got stuck with how to reset the 
        canvas background to white. The solution is so simple - add the line self.canvas.config(bg="white") 
        to the get_next_question method.
        """
        self.window.after(1000, self.get_next_question)