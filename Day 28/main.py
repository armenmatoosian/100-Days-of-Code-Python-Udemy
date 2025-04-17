import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
# my code and solution code for Adding Checkmarks and Resetting the Application
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
# code for Pomodoro Project: Add a Countdown Mechanism
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # # my code for Setting Different Timer Sessions and Values
    # if reps == 0 or reps == 2 or reps == 4 or reps == 6:
    #     count_down(work_sec)
    #     reps += 1
    # elif reps == 1 or reps == 3 or reps == 5:
    #     count_down(short_break_sec)
    #     reps += 1
    # elif reps == 7:
    #     count_down(long_break_sec)
    #     reps += 1

    # solution code for Setting Different Timer Sessions and Values
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED) # my code, same as solution
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)  # my code, same as solution
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)  # my code, same as solution

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# code for Pomodoro Project: Add a Countdown Mechanism
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer() # solution code for Setting Different Timer Sessions and Values
        # # my code for Adding Checkmarks and Resetting the Application (doesn't work)
        # if reps % 2 == 0 or reps % 8 == 0:
        #     add_checkmark()

        # solution code for Adding Checkmarks and Resetting the Application
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        checkmark_label.config(text=marks)

# # my code for Adding Checkmarks and Resetting the Application (doesn't work)
# def add_checkmark():
#     checkmark_label.config(text="✓", fg=GREEN, bg=YELLOW, highlightthickness=0)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# my code for Pomodoro Project: Complete the Application's User Interface (UI) - same as solution
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark_label = Label(fg=GREEN, bg=YELLOW, highlightthickness=0)
checkmark_label.grid(column=1, row=3)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 35))
timer_label.grid(column=1, row=0)



window.mainloop()