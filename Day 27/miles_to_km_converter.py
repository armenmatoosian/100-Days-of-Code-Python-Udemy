# my code for Mile to Kilometers Converter Project
from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
#adding padding
window.config(padx=20, pady=20)

#labels
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)
miles = Label(text="Miles")
miles.grid(column=2, row=0)
kilometres = Label(text="Km")
kilometres.grid(column=2, row=1)
kilometres_value = Label(text=0)
kilometres_value.grid(column=1, row=1)

#input
miles_entry = Entry(width=30)
miles_entry.grid(column=1, row=0)

def convert():
    converted_value = int(miles_entry.get()) * 1.609344 #original code

    kilometres_value.config(text=converted_value)

calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)

window.mainloop()


# # solution code for Mile to Kilometers Converter Project
# from tkinter import *
#
# def miles_to_km():
#     miles = float(miles_input.get())
#     km = miles * 1.609
#     kilometre_result_label.config(text=f"{km}")
#
# window = Tk()
# window.title("Miles to Kilometre Converter")
# window.config(padx=20, pady=20)
#
# miles_input = Entry(width=7)
# miles_input.grid(column=1, row=0)
#
# miles_label = Label(text="Miles")
# miles_label.grid(column=2, row=0)
#
# is_equal_label = Label(text="is equal to")
# is_equal_label.grid(column=0, row=1)
#
# kilometre_result_label = Label(text="0")
# kilometre_result_label.grid(column=1, row=1)
#
# kilometre_label = Label(text="Km")
# kilometre_label.grid(column=2, row=1)
#
# calculate_button = Button(text="Calculate", command=miles_to_km)
# calculate_button.grid(column=1, row=2)
#
#
# window.mainloop()