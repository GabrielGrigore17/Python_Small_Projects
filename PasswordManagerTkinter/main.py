from tkinter import *
from tkinter import messagebox
import random
import json
import pyperclip


def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            website = website_entry.get()
            if data.get(website):
                password = data.get(website).get("password")
                email = data.get(website).get("email")
                messagebox.showinfo(title=website, message=f"Email: {email} \n Password: {password}")
            else:
                messagebox.showerror(title="ERROR", message=f"Found no entry for {website}")
    except FileNotFoundError:
        messagebox.showerror(title="ERROR", message="The file is empty!")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list.extend(random.choice(letters) for _ in range(nr_letters))
    password_list.extend(random.choice(symbols) for _ in range(nr_symbols))
    password_list.extend(random.choice(numbers) for _ in range(nr_numbers))

    random.shuffle(password_list)

    password_generated = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password_generated)
    pyperclip.copy(password_generated)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email_username = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password,
        }
    }
    if not len(website) or not len(password):
        messagebox.showerror(title="ERROR", message="Empty fields are not valid!")
        return
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details: \nEmail: {email_username}"
                                                          f"\nPassword: {password} \n Is it ok to save?")

    if is_ok:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()
email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "gabigrigore17@gmail.com")
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)
add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="EW")


window.mainloop()
