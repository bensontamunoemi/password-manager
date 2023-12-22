import json
from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip


# ---------------------------- FILE SETUP ------------------------------- #
def save():
    """Save data to file"""
    website = entry_website.get()
    email = entry_email_uname.get()
    password = entry_password.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning!", message="No fields should be left empty")
    else:
        try:
            print("HERRE ")

            with open("data.json", "r") as password_file:
                # Read File
                data = json.load(password_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):

            with open("data.json", "w") as password_file:
                # Save updated data
                json.dump(new_data, password_file, indent=4)
        else:
            print("HERRE 2")

            # Update File
            data.update(new_data)
            with open("data.json", "w") as password_file:
                # Save updated data
                json.dump(data, password_file, indent=4)
        finally:
            print("HERRE 3")

            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    small_letters = ["a", "b", "c", "d", "e", "f",
                     "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                     "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    capital_letters = ["A", "B", "C", "D", "E", "F",
                       "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                       "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "@", "#", "$", "%", "&", "*", "(", ")", "+"]

    selected_small_letters = [choice(small_letters) for _ in range(randint(8, 10))]
    selected_capital_letters = [choice(capital_letters) for _ in range(randint(8, 10))]
    selected_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    selected_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = selected_small_letters + selected_numbers + selected_symbols + selected_capital_letters
    shuffle(password_list)

    password = "".join(password_list)
    if len(entry_password.get()) > 0:
        entry_password.delete(0, END)
        entry_password.insert(0, password)
    else:
        entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)
window.resizable(False, False)

canvas = Canvas(width=360, height=360)
tomato_img = PhotoImage(file="padlock.png")
canvas.create_image(180, 180, image=tomato_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

entry_website = Entry()
entry_website.grid(column=1, row=1, columnspan=2, sticky="EW")
entry_website.focus()

label_email_uname = Label(text="Email/Username:")
label_email_uname.grid(column=0, row=2)

entry_email_uname = Entry()
entry_email_uname.grid(column=1, row=2, columnspan=2, sticky="EW")
entry_email_uname.insert(0, "bensontamunoemi@gmail.com")

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", width=35, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

mainloop()
