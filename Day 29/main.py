from tkinter import *
from tkinter import messagebox # code for Dialog Boxes and Pop-Ups in Tkinter
# # starting code needed for my code
# import random
# solution code
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #Password Generator Project - modified solution code from Day 5: Beginner - Python Loops
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # # starting code needed for my code
    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)

    # # my code for Generate a Password & Copy it to the Clipboard - converting a loop to a list comprehension
    # password_list = []
    #
    # # # original loop
    # # for char in range(nr_letters):
    # #   password_list.append(random.choice(letters))
    # password_list += [random.choice(letters) for letter_char in range(nr_letters)]
    #
    # # # original loop
    # # for char in range(nr_symbols):
    # #   password_list += random.choice(symbols)
    # password_list += [random.choice(symbols) for symbol_char in range(nr_symbols)]
    #
    # # # original loop
    # # for char in range(nr_numbers):
    # #   password_list += random.choice(numbers)
    # password_list += [random.choice(numbers) for number_char in range(nr_numbers)]
    #
    # random.shuffle(password_list)
    #
    # password = ""
    #
    # # # original
    # # for char in password_list:
    # #   password += char
    # password += password.join(password_list)
    # print(f"Your password is: {password}") # this is for checking only

    # solution code for Generate a Password & Copy it to the Clipboard - converting a loop to a list comprehension
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    # my code for inserting generated password into entry field, Password - same as solution code
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# # my code for Challenge 3 - Saving Data to File, works but different from solution code
# def save():
#     global website, email, password
#     saved_passwords = open("data.txt", "a") # started to use with open() but forgot it automatically closes the file after writing to it
#     saved_passwords.write(f"{website.get()} | {email.get()} | {password.get()}\n")
#     saved_passwords.close()
#     website_entry.delete(0, END)
#     email_entry.delete(0, END) # unnecessary, unless you want to set a default email address
#     email_entry.insert(0, "armen@gmail.com") # unnecessary, unless you want to set a default email address
#     password_entry.delete(0, END)

# solution code for Challenge 3 - Saving Data to File
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # solution code for Dialog Boxes and Pop-Ups in Tkinter
    if len(website) == 0 or len(password) == 0: # solution code for Dialog Boxes and Pop-Ups in Tkinter
        messagebox.showerror(title="Error", message="Please don't leave any fields empty!") # solution code for Dialog Boxes and Pop-Ups in Tkinter
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details enter: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

    # # my code for Dialog Boxes and Pop-Ups in Tkinter, works but slightly different logic from solution
    # is_ok = True # my code for Dialog Boxes and Pop-Ups in Tkinter
    #
    # if website == "" or email == "" or password == "": # my code for Dialog Boxes and Pop-Ups in Tkinter
    #     messagebox.showerror(title="Oops", message="Please don't leave any fields empty!") # my code for Dialog Boxes and Pop-Ups in Tkinter
    #     is_ok = False # my code for Dialog Boxes and Pop-Ups in Tkinter
    # elif is_ok:
    #     is_ok = messagebox.askokcancel(title=website, message=f"These are the details enter: \nEmail: {email} "
    #                                                           f"\nPassword: {password} \nIs it ok to save?")
    #     with open("data.txt", "a") as data_file:
    #         data_file.write(f"{website} | {email} | {password}\n")
    #         website_entry.delete(0, END)
    #         password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# my code for Challenge 1 - Working with Images and Setting up the Canvas, same as solution with minor differences
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# my code for Challenge 2 - Use grid() and columnspan to Complete the User Interface, same as solution with minor differences
# buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save) # my code for Challenge 3 - Saving Data to File
add_button.grid(column=1, row=4, columnspan=2)

# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# entries
website_entry = Entry(width=51)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
# website = website_entry # my code for Challenge 3 - Saving Data to File

email_entry = Entry(width=51)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "armen@gmail.com")
# email = email_entry # my code for Challenge 3 - Saving Data to File

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)
# password = password_entry # my code for Challenge 3 - Saving Data to File

window.mainloop()