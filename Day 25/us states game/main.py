import turtle
import pandas as pd


screen = turtle.Screen()
screen.title('States game of U.S. ')
bg = 'blank_states_img.gif'
screen.addshape(bg)
turtle.shape(bg)

df = pd.read_csv('50_states.csv')
state_list = df['state'].to_list()
guessed_states = []

while len(guessed_states) < 50:
    
    answer_state = screen.textinput(f'{len(guessed_states)}/50 States', "What's another states name?").title()
    if answer_state in state_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_info = df[df['state'] == answer_state]
        t.goto(int(state_info['x']), int(state_info['y']))
        t.write(answer_state)
    elif answer_state == 'Exit':
        missing_states = []
        for i in state_list:
            if i not in guessed_states:
                missing_states.append(i)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('Missing_states_list.csv')
        break

