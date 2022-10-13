import tkinter as tk
THEME_COLOR = "#375362"
FONT_NAME = ('arial', 12)

class QuizUI:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Quizz App')
        self.window.config(bg=THEME_COLOR, padx= 20, pady=20)

        self.score_label = tk.Label(text=f'score: 0', bg=THEME_COLOR,
                    fg='white', font=FONT_NAME)
        self.score_label.grid(row=0, column=1, sticky='EW')

        self.canvas=tk.Canvas(width=300, height=350, bg='white')
        self.question_text = self.canvas.create_text((150,125),text='Question text', fill=THEME_COLOR,
                            font=('Arial',15))
        self.canvas.grid(row=1, column=0, columnspan= 2,
                         sticky='EW', pady=50)
        
        tick_img = tk.PhotoImage(file=r'Day 34\images\true.png')
        cross_img = tk.PhotoImage(file=r'Day 34\images\false.png')


        self.button_yes = tk.Button(image=tick_img,highlightthickness=0,
                        bg=THEME_COLOR)
        self.button_yes.grid(column=0, row=2, sticky='EW')
        self.button_no = tk.Button(image=cross_img, highlightthickness=0,
                        bg=THEME_COLOR)
        self.button_no.grid(column=1, row=2, sticky='EW')


        self.window.mainloop()