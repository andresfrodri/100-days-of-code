from tkinter import *

def result():
    num=int(input.get())*1.609
    my_label3.config(text=num)



window = Tk()
window.title('Mile to km converter')
window.minsize(250, 100)
window.config(padx=10, pady=10)

#Creating components inside the window

#Labels

my_label1 = Label(text='   Miles', font = ('Arial', 14))
my_label1.grid(column=2, row=0)

my_label2 = Label(text='is equal to', font = ('Arial', 14))
my_label2.grid(column=0, row=1)

my_label3 = Label(text='0', font = ('Arial', 14))
my_label3.grid(column=1, row=1)

my_label4 = Label(text='km', font = ('Arial', 14))
my_label4.grid(column=2, row=1)



#Entry

input = Entry(width=13)
input.grid(column=1, row=0)

#Button
button = Button(text='Calculate', command= result)
button.grid(column=1, row=2)


window.mainloop()
