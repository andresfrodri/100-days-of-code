import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = ('arial', 25, 'bold')
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps=0
timer = None 
# ---------------------------- TIMER RESET ------------------------------- # 
def reseter():
    window.after_cancel(timer)
    title_label.config(text='Timer')
    canvas.itemconfig(timer_text, text='00:00')
    check_label.config(text='')
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def raise_window(window):
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    s_break_sec= SHORT_BREAK_MIN*60
    l_break_sec = LONG_BREAK_MIN*60
    if reps%2 !=0:
        count_down(work_sec)
        title_label.config(text='WORKING')
        reps += 1
    elif reps %8 == 0:
        count_down(l_break_sec)
        title_label.config(text='Long break')
        reps += 1
    else:
        count_down(s_break_sec)
        title_label.config(text='Short break')
        reps += 1



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(number):
    global timer
    num_min = math.floor(number/60)
    num_sec= number%60

    canvas.itemconfig(timer_text, text=f'{num_min:02}:{num_sec:02}')
    if number>0:
        timer = window.after(1000, count_down, number-1)
    else:
        raise_window(window)
        start_timer()
        marks = ''
        work_sessions=math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✓"
        check_label.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Pomodoro project')
window.config(padx=100, pady= 50, bg=YELLOW)



canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100, 120, text='00:00', fill='white', font=FONT_NAME )


canvas.grid(column=1,row=1)

#Label
title_label = tkinter.Label(text="Timer", font=FONT_NAME, bg=YELLOW)
title_label.grid(row=0, column=1)

check_label = tkinter.Label(font=('arial', 20, 'bold'), bg=YELLOW, fg=GREEN)
check_label.grid(row=3, column=1)


#Buttons 
button1 = tkinter.Button(text='Start', highlightthickness=0, command=start_timer)
button1.grid(column=0, row=2)

button2 = tkinter.Button(text='Reset', highlightthickness=0, command=reseter)
button2.grid(column=2, row=2)

window.mainloop()