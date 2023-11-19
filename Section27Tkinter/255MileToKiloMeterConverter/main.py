from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)


# Entry

input = Entry(width=20)
input.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)


#  Label
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

# Label
total_km_label = Label(text=0)
total_km_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)



# Button

def button_clicked():
    miles = input.get()
    km = int(miles) * 1.609
    total_km_label.config(text=km)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)


window.mainloop()