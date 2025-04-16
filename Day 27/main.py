"""
code for:
- Creating Windows and Labels with Tkinter
- Setting Default Values for Optional Arguments inside a Function Header
"""

from tkinter import *

#Buttons
def button_clicked():
    print("I got clicked")
    # my_label.config(text=input.get()) #my code
    #solution code
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
#adding padding
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24))
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# code for Buttons, Entry, and Setting Component Options

#Buttons
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="Click Me!", command=button_clicked)
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
input.get()
# input.pack()
input.grid(column=3, row=2)


window.mainloop()