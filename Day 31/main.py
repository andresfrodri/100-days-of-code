import tkinter
import pandas as pd
import random as rd


#-------------------Constants--------------------#
BACKGROUND_COLOR = "#B1DDC6"
title_font=('Ariel',40,'italic')
word_font=('Ariel',60,'bold')

#----------------functions------------------------#
def word_choicer():
    
    pass

#----------------Import the information------------#

info=pd.read_csv('german - english.csv')
info = info.to_dict()

#--------------------UI----------------------------#
window = tkinter.Tk()
window.title('Flash cards!')

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = tkinter.PhotoImage(file='images\card_front.png')
back_img = tkinter.PhotoImage(file='images\card_back.png')
canvas.create_image(400,263, image=front_img) 

title_text = canvas.create_text(400, 150, text='title', font=title_font)
word_text = canvas.create_text(400, 263, text='word', font=word_font)

canvas.grid(column=0, row=0, columnspan=2,sticky='EW')

tick_img=tkinter.PhotoImage(file=r'images\right.png')
cross_img=tkinter.PhotoImage(file='images\wrong.png')


#Buttons

tick_button = tkinter.Button(text='', image=tick_img,highlightthickness=0, bg=BACKGROUND_COLOR)
tick_button.grid(column=0, row=1, sticky='EW')

cross_button = tkinter.Button(image=cross_img,highlightthickness=0, bg=BACKGROUND_COLOR)
cross_button.grid(column=1, row=1, sticky='EW')


window.mainloop()