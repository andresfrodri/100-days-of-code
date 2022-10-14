from cgitb import text
import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT_NAME = ('arial', 12)


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title('Quizz App')
        self.window.config(bg=THEME_COLOR, padx= 20, pady=20)

        
        self.score_label = tk.Label(text=f'score: 0', bg=THEME_COLOR,
                    fg='white', font=FONT_NAME)
        self.score_label.grid(row=0, column=1, sticky='EW')

        self.canvas=tk.Canvas(width=300, height=350, bg='white')
        self.question_text = self.canvas.create_text((150,125),text='Question text', fill=THEME_COLOR,
                            font=('Arial',15), width=280)
        self.canvas.grid(row=1, column=0, columnspan= 2,
                         sticky='EW', pady=50)
        
        tick_img = tk.PhotoImage(file=r'Day 34\images\true.png')
        cross_img = tk.PhotoImage(file=r'Day 34\images\false.png')


        self.button_yes = tk.Button(image=tick_img,highlightthickness=0,
                        bg=THEME_COLOR, command= self.true_a, bd=0)
        self.button_yes.grid(column=0, row=2)
        self.button_no = tk.Button(image=cross_img, highlightthickness=0,
                        bg=THEME_COLOR, command=self.false_a, bd=0)
        self.button_no.grid(column=1, row=2)
        self.get_q()


        self.window.mainloop()

    def get_q(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f'You ended the quiz \n Your final score was: {self.quiz.score}/{self.quiz.question_number}')
            self.button_yes.config(state='disabled')
            self.button_no.config(state='disabled')    
    def false_a(self):
        self.give_fb(self.quiz.check_answer('True'))

    def true_a(self):
        self.give_fb(self.quiz.check_answer('False'))
    

    def give_fb(self,a_ans):
        if a_ans == True:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        
        self.window.after(1000, self.get_q)
    
