from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUi:
    
    def __init__(self , quiz_brain: QuizBrain ):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20 , pady=20 , bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white" , bg=THEME_COLOR)
        self.score_label.grid(row=0 , column=1)

        self.canvas = Canvas(width=300 , height=250 , bg="white")
        self.question = self.canvas.create_text(150, 125, 
                                                 text="some text" , 
                                                 width = 280 ,
                                                 fill=THEME_COLOR , 
                                                 font=("Arial",20,"italic"))
        self.canvas.grid(row = 1, column=0 , columnspan=2 , pady=50)
        
        self.tick_img = PhotoImage(file="quizz game/images/true.png")
        self.cross_img = PhotoImage(file="quizz game/images/false.png")

        self.true_button = Button(image=self.tick_img, highlightthickness=0 , command=self.true)
        self.true_button.grid(row=2 , column=0)
        self.false_button = Button(image=self.cross_img, highlightthickness=0 , command=self.false)
        self.false_button.grid(row=2 , column=1)

        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question , text=q_text)
        else:
            self.canvas.itemconfig(self.question , text = "You have reached the end of the quizz game.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000  , self.get_next_question)