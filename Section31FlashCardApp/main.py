from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
timer = 3
random_selection = None


# ------ Data Setup --------#

try:
    csv_data = pandas.read_csv("Section31FlashCardApp\data\\words_to_learn.csv")
except FileNotFoundError:
    csv_data = pandas.read_csv("Section31FlashCardApp\data\\french_words.csv")
finally:
    dictionary_data = csv_data.to_dict(orient="records")

# ------ Timer Reset --------#

def reset_timer():
    window.after_cancel(timer)

# ------ Countdown --------#

def count_down(count):
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        window.after_cancel(timer)
        canvas.itemconfig(canvas_image, image=card_back)
        french_label.config(fg="white", bg="#91C2AF", text="English")
        global random_selection
        french_word_label.config(fg="white", bg="#91C2AF", text=random_selection["English"])
        
        
# ------ Button Functions --------#

def knows_word():
    remove_from_list()
    next_card()

def does_not_know_word():
    try:
        words_to_learn_csv = pandas.read_csv("Section31FlashCardApp\data\\words_to_learn.csv")
        words_to_learn_dictionary = words_to_learn_csv.to_dict(orient="records")
    except FileNotFoundError:
        words_to_learn_dictionary = [random_selection]
    else:
        words_to_learn_dictionary.append(random_selection)
    finally:
        df = pandas.DataFrame(words_to_learn_dictionary)
        df.to_csv(path_or_buf="Section31FlashCardApp\data\\words_to_learn.csv", index=False)
        remove_from_list()
        next_card()
        
     
# ------ Remove From Dictionary And CSV --------#

def remove_from_list():
    dictionary_data.remove(random_selection)    

# ------ Next Card --------#

def next_card():
    if len(dictionary_data) == 0:
        french_label.config(text="All done!")
        french_word_label.config(text="Restart the program to reset the cards", font=("Ariel", 15, "bold"))
    else:
        canvas.itemconfig(canvas_image, image=card_front)
        global random_selection
        random_selection = random.choice(dictionary_data)
        french_word_label.config(text=random_selection["French"], fg="black", bg="#FFFFFF",)
        french_label.config(text="English", fg="black", bg="#FFFFFF",)
        count_down(3)

# ------ UI Setup --------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="Section31FlashCardApp\images\card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=1, row=1, columnspan=3, rowspan=2)
card_back = PhotoImage(file="Section31FlashCardApp\images\card_back.png")

# Buttons

wrong_image = PhotoImage(file="Section31FlashCardApp\images\wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=does_not_know_word)
wrong_button.grid(column=1, row=3)

right_image = PhotoImage(file="Section31FlashCardApp\images\\right.png")
right_button = Button(image=right_image, highlightthickness=0, command=knows_word)
right_button.grid(column=3, row=3)

#  Labels
french_label = Label(text="French", font=("Ariel", 40, "italic"), bg="#FFFFFF")
french_label.grid(column=2, row=1)

french_word_label = Label(text="", font=("Ariel", 60, "bold"), bg="#FFFFFF")
french_word_label.grid(column=2, row=2)


next_card()

window.mainloop()