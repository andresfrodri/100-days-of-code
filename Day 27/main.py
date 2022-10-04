import tkinter

window = tkinter.Tk()
window.title('First GUI program')
window.minsize(500, 400)

#Creating components inside the window
#Label

my_label = tkinter.Label(text='My fisrt label', font = ('Arial', 24))
my_label.pack(expand= True)








window.mainloop()