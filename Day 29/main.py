import tkinter
from tkinter import messagebox
import random
import json
import pyperclip


FONT_NAME = ('arial', 12)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
options_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2',
 '3', '4', '5', '6', '7', '8', '9' ,'!', '#', '$', '%', '&', '(', ')', '*', '+']
def password_gen():
    password_entry.delete(0,'end')
    s=''
    for i in range(12):
        i=random.choice(options_list)
        s+=i
    password_entry.insert(0,s) 
    pyperclip.copy(s)
    
# ---------------------------- PASSWORD SEARCHER ------------------------------- #
def searcher():
    website=website_entry.get()
    try:
        with open('data.json','r') as data_file:
            #Reading old data
            data=json.load(data_file) #used to read
            web_dict=data[website]
    except KeyError:
        messagebox.showinfo('Error', message='No data found for that website')
    except FileNotFoundError:
        messagebox.showinfo('Error', message='No data file found/No saved passwords')
    else:
        messagebox.showinfo(website, message=f'Username: {web_dict["username"]} \n Password: {web_dict["password"]}')
    



# ---------------------------- SAVE PASSWORD ------------------------------- #
def create_data(website, username, password):
    new_data = {
        website:{
            'username': username,
            'password': password,
        }    
    }
    try:
        with open('data.json','r') as data_file:
            #Reading old data
            data=json.load(data_file) #used to read
    except FileNotFoundError:
        with open('data.json','w') as data_file:
        #creates the files
            json.dump(new_data, data_file, indent=5) #used to write
        create_data(website, username, password)
    else:
        #Updating old data with new data
        data.update(new_data)
        with open('data.json','w') as data_file:
            #Saving the updating data
            json.dump(data, data_file, indent=5) #used to write


def deleting():
    website_entry.delete(0, 'end')
    username_entry.delete(0, 'end')
    username_entry.insert(0, '@gmail.com')
    password_entry.delete(0, 'end')
    
def save():
    website=website_entry.get()
    username=username_entry.get()
    password = password_entry.get()
    if username == '' or password == '':
        is_ok2=messagebox.showwarning(title='WARNING', message='One of the fields is empty')
    else:
        create_data(website, username, password)
        deleting()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

#Background image

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
lock_img = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100,100, image=lock_img) 
canvas.grid(row=0, column=1)

#labels
website_label = tkinter.Label(text="Website:", font=FONT_NAME)
website_label.grid(row=1, column=0)

username_label = tkinter.Label(text="Email/Username:", font=FONT_NAME)
username_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password:", font=FONT_NAME)
password_label.grid(row=3, column=0)

#Buttons
generate_button = tkinter.Button(text='Generate Password', highlightthickness=0, command=password_gen)
generate_button.grid(column=2, row=3)

add_button = tkinter.Button(text='Add', highlightthickness=0, width=40, command=save)
add_button.grid(column=1, row=4, columnspan=2,sticky='EW')

search_button = tkinter.Button(text='Search', highlightthickness=0, command=searcher)
search_button.grid(column=2, row=1,sticky='EW')
#Entries
website_entry = tkinter.Entry()
website_entry.focus()
website_entry.grid(row=1, column=1,sticky='EW')

username_entry = tkinter.Entry()
username_entry.insert(0, '@gmail.com')
username_entry.grid(row=2, column=1,columnspan=2,sticky='EW')

password_entry = tkinter.Entry(show="*")
password_entry.grid(row=3, column=1,sticky='EW')


window.mainloop()