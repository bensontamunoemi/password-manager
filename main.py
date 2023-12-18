from tkinter import *
from tkinter import messagebox


# ---------------------------- FILE SETUP ------------------------------- #
def save():
    """Save data to file"""
    website = entry_website.get()
    email = entry_email_uname.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning!", message="No fields should be left empty")
    else:
        is_okay = messagebox.askokcancel(title=website,
                                         message=f"These are the details entered: \nEmail: {email} "
                                                 f"\nPassword: {password} \n Website: {website} \n Is it okay to save?")
        if is_okay:
            with open("data.txt", "a") as password_file:
                password_file.write(f"{website} | {email} | {password}\n")
                entry_website.delete(0, END)
                entry_password.delete(0, END)


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

generate_btn = Button(text="Generate Password")
generate_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", width=35, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

mainloop()
