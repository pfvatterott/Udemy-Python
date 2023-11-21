from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    
    
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", font=("Ariel", 15, "italic"), width=290)
        self.canvas.grid(column=1, row=2, columnspan=2, pady=40)
        
        
        # Buttons
        false_image = PhotoImage(file="Section34APIGUIQuizApp\\307ClassBasedTkinterUI\images\\false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_check_answer)
        self.false_button.grid(column=2, row=3)

        true_image = PhotoImage(file="Section34APIGUIQuizApp\\307ClassBasedTkinterUI\images\\true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_check_answer)
        self.true_button.grid(column=1, row=3)
        
        #  Labels
        self.score_label = Label(text="Score: 0", font=("Ariel", 10, "bold"), bg="#375362", fg="white")
        self.score_label.grid(column=2, row=1)

        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        
    def true_check_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
            
        
    def false_check_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)