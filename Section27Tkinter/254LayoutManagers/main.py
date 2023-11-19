from tkinter import *


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# Label
my_label = Label(text="I am a Label", font=("Arial", 24))
my_label["text"] = "New Text"
my_label.config(text="New new text")
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


# Button

def button_clicked():
    my_label.config(text=input.get())

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)



# Entry

input = Entry(width=20)
input.grid(column=3, row=2)


# Button 2
button2 = Button(text="Button2")
button2.grid(column=2, row=0)


window.mainloop()