from turtle import Turtle
from turtle import Screen
import pandas

screen = Screen()

screen.bgpic('blank_states_img.gif')
screen.setup(700, 500)

states_guessed = 0

data = pandas.read_csv('50_states.csv')

dict_data = {}

states_name = data['state'].to_list()
cox_state = data['x'].to_list()
coy_state = data['y'].to_list()


def show_name(name, position):
    state = Turtle()
    state.hideturtle()
    state.penup()
    state.goto(position)
    state.write(name, move=True, font=('Arial', 8, 'normal'))
    state.color('white')


for i in range(len(states_name)):
    dict_data[states_name[i]] = (cox_state[i], coy_state[i])

while states_guessed != 50:
    user_input = screen.textinput(f'Guess state', f'Enter the state name of {states_guessed}/50')
    if user_input is not None:
        user_input = user_input.title()
    else:
        break
    if user_input in dict_data:
        pos = dict_data[user_input]
        print(f'{pos}')
        show_name(user_input, pos)
        dict_data.pop(user_input)
        states_guessed += 1

write = ('Congratulations', 'Game Over')

end_it = Turtle()
end_it.hideturtle()
end_it.write(write[50 != states_guessed], font=('Arial', 16, 'bold'))




screen.exitonclick()