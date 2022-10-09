import tkinter
import pandas as pd
import random as rd


#-------------------Constants--------------------#
BACKGROUND_COLOR = "#B1DDC6"
title_font=('Arial',40,'italic')
word_font=('Arial',60,'bold')
a=1
#----------------functions------------------------#
def wordle():
    word_de=rd.choice(info_dict_keys)
    word_en=info_dict[word_de]
    return (word_de, word_en)

def new_flash():
    global a
    global word_tup
    word_de=rd.choice(info_dict_keys)
    word_en=info_dict[word_de]
    word_tup=(word_de, word_en)
    a=1
    sign_fun()
    

   
def sign_fun():
    global a
    a*=-1
    if a<0:
        canvasf.create_image(400,263, image=front_img) 
        title_text = canvasf.create_text(400, 150, text='German', font=title_font)
        word_text = canvasf.create_text(400, 263, text=word_tup[0], font=word_font)
    else:
        canvasf.create_image(400,263, image=back_img) 
        title_text = canvasf.create_text(400, 150, text='English', font=title_font)
        word_text = canvasf.create_text(400, 263, text=word_tup[1], font=word_font)
    canvasf.grid(column=0, row=0, columnspan=2,sticky='EW')


def combiner():
    word_de=rd.choice(info_dict_keys)
    word_en=info_dict[word_de]

#----------------Import the information------------#

info=pd.read_csv('german - english.csv')

info_dict ={row['German']:row['English'] for (index, row) in info.iterrows()}
info_dict_keys=list(info_dict.keys())

#--------------------UI----------------------------#
window = tkinter.Tk()
window.title('Flash cards for german!')

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvasf = tkinter.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

front_img = tkinter.PhotoImage(file='images\card_front.png')
back_img = tkinter.PhotoImage(file='images\card_back.png')
word_tup=wordle()
new_flash()

tick_img=tkinter.PhotoImage(file=r'images\right.png')
cross_img=tkinter.PhotoImage(file='images\wrong.png')


#Buttons

tick_button = tkinter.Button(text='', image=tick_img,highlightthickness=0, bg=BACKGROUND_COLOR, command=new_flash)
tick_button.grid(column=0, row=1, sticky='EW')

cross_button = tkinter.Button(image=cross_img,highlightthickness=0, bg=BACKGROUND_COLOR, command=sign_fun)
cross_button.grid(column=1, row=1, sticky='EW')

print(a)
window.mainloop()