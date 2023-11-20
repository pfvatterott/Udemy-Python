from tkinter import *
from tkinter import messagebox
import random
import pyperclip
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = ""
    password = "".join(password_list)

    password_entry.insert(0, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(password) == 0 or len(email) == 0 or len(website) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty!")
        
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nOk to save?")
        
        if is_ok:
            with open('Section29PasswordManager\\264Challenge1\data.txt', mode="a") as file:
                file.write(f"{website} | {email} | {password} \n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)



# Canvas
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="Section29PasswordManager\\264Challenge1\logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=2, row=1)


#  Labels
website_label = Label(text="Website:", font=(FONT_NAME, 12))
website_label.grid(column=1, row=2)

email_label = Label(text="Email/Username:", font=(FONT_NAME, 12))
email_label.grid(column=1, row=3)

password_label = Label(text="Password:", font=(FONT_NAME, 12))
password_label.grid(column=1, row=4)


#Entries
website_entry = Entry(width=40)
website_entry.grid(column=2, row=2, columnspan=2)
website_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(column=2, row=3, columnspan=2)
email_entry.insert(0, "pfvatterott@gmail.com")

password_entry = Entry(width=22)
password_entry.grid(column=2, row=4, columnspan=1)


# Buttons

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=3, row=4)

add_button = Button(text="Add", width=34, command=save_password)
add_button.grid(column=2, row=5, columnspan=2)


window.mainloop()