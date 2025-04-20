from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    # modifying original code from Day 29 Password Manager to use JSON
    else:
        try:
        # solution code for Challenge 1 - Handling Exceptions in the Password Manager
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open(f"data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        # # my code for Challenge 1 - Handling Exceptions in the Password Manager
        # except FileNotFoundError:
        #     with open("data.json", "w") as data_file:
        #         json.dump(new_data, data_file, indent=4)
        #     save()
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
# my code for Challenge 2 - Search for a Website in the Password Manager, create find_password() and error handling
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            messagebox.showinfo(title="Website Search", message=f"Email: {data[website]["email"]}\n"
                                                                f"Password: {data[website]["password"]}")
            website_entry.delete(0, END)
    except FileNotFoundError:
        messagebox.showinfo(title="Website Search", message=f"No Data File Found.")
    except KeyError:
        messagebox.showinfo(title=f"Website: {website} Not Found", message=f"No details for the website exist.")

    # # solution code for Challenge 2 - Search for a Website in the Password Manager, create find_password() and error handling
    # website = website_entry.get()
    # try:
    #     with open("data.json") as data_file:
    #         data = json.load(data_file)
    # except FileNotFoundError:
    #     messagebox.showinfo(title="Error", message=f"No Data File Found.")
    # else:
    #     if website in data:
    #         email = data[website]["email"]
    #         password = data[website]["password"]
    #         messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
    #     else:
    #         messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# my code for Challenge 2 - Search for a Website in the Password Manager, modified pre-existing entries and buttons
#Entries
website_entry = Entry(width=34)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)
# my code for Challenge 2 - Search for a Website in the Password Manager, added search button
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()