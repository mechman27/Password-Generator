from tkinter import *
from quiz_brain import QuizBrain
FONT = ("arial",20,"italic")
THEME_COLOR = "#375362"



class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Brain")
        self.window.config(padx = 20, pady = 20, bg=THEME_COLOR)
        
        self.score_label = Label(text=f"Score = {self.quiz.score}", 
                    fg="white", 
                    bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, 
                    text="Something",
                    fill=THEME_COLOR, 
                    font=FONT, 
                    width=280)
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)
        
        TRUE_IMAGE = PhotoImage(file="Intermediate/Day 34 Quiz Update/images/true.png")
        FALSE_IMAGE = PhotoImage(file="Intermediate/Day 34 Quiz Update/images/false.png")
        self.true_button = Button(image=TRUE_IMAGE, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=FALSE_IMAGE,highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2,column=1)
        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.false_button.config(state = "disabled")
            self.true_button.config(state = "disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)