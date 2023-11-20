from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
FONT_NAME = "Courier"

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showinfo(title="Error", message="Please type in a website to search for!")
    else:
        try:
            with open('Section30ErrorsExceptionsAndJSON/276PasswordManagerUpdate/data.json', mode="r") as file:
                data = json.load(file)
                email_and_password = data[website]
        except FileNotFoundError and KeyError:
            messagebox.showinfo(title="Error", message="Could not find saved password!")
        else:
            messagebox.showinfo(title="Success", message=f"Email: {email_and_password["email"]} \nPassword: {email_and_password["password"]}")
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
        


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)
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
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    
    if len(password) == 0 or len(email) == 0 or len(website) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty!")
        
    else:
        try:
            with open('Section30ErrorsExceptionsAndJSON/276PasswordManagerUpdate/data.json', mode="r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open('Section30ErrorsExceptionsAndJSON/276PasswordManagerUpdate/data.json', mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open('Section30ErrorsExceptionsAndJSON/276PasswordManagerUpdate/data.json', mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)



# Canvas
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="Section30ErrorsExceptionsAndJSON/276PasswordManagerUpdate/logo.png")
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
website_entry = Entry()
website_entry.grid(column=2, row=2)
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

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=3, row=2)


window.mainloop()