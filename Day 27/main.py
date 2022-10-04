from tkinter import *
def button_clicked():
    my_label.config(text=input.get())


window = Tk()
window.title('First GUI program')
window.minsize(500, 400)
window.config(padx=20, pady=20)

#Creating components inside the window
#Label

my_label = Label(text='My first label', font = ('Arial', 24))

my_label['text']='Hellooo'
my_label.config(text='Helooooo')
my_label.grid(column=0, row=0)

#Buttons

button = Button(text='Click me to change title', command= button_clicked)
button.grid(column=1, row=1)


new_button = Button(text='Hi', command= button_clicked)
new_button.grid(column=2, row=0)
#Entry

input = Entry(width=13)
input.grid(column=3, row=2)






window.mainloop()