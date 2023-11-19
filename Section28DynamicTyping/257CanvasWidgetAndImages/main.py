from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    time_label.config(text="Timer", fg=GREEN)
    check_mark_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    
    if reps % 2 != 0:
        count_down(WORK_MIN * 60)
        time_label.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        time_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        time_label.config(text="Short Break", fg=PINK)
 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    if count_minutes < 10:
        count_minutes = f"0{count_minutes}"
    count_text = f"{count_minutes}:{count_seconds}"
    canvas.itemconfig(timer_text, text=count_text)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check_mark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#  Label
time_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
time_label.grid(column=2, row=1)

# Canvas
canvas = Canvas(width=206, height=224, bg=YELLOW, highlightthickness=0)
tom_image = PhotoImage(file="Section28DynamicTyping\\257CanvasWidgetAndImages\\tomato.png")
canvas.create_image(103, 112, image=tom_image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=2, row=2)


# Start Button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=3)


# Reset Button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=3)

# Check mark Label
check_mark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_mark_label.grid(column=2, row=4)


window.mainloop()