from tkinter import *


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# Label
my_label = Label(text="I am a Label", font=("Arial", 24))
my_label.pack()
my_label["text"] = "New Text"
my_label.config(text="New new text")



# Button

def button_clicked():
    my_label.config(text=input.get())

button = Button(text="Click Me", command=button_clicked)
button.pack()


# Entry

input = Entry(width=20)
input.pack()


window.mainloop()