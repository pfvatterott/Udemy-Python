import turtle
import pandas
from state import State

screen = turtle.Screen()
screen.title = "US States Game"
image = "Section25CSVDataAndPandas\\231USStatesGame\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_is_on = True
state_data = pandas.read_csv("Section25CSVDataAndPandas\\231USStatesGame\\50_states.csv")
all_states = state_data.state.str.lower().to_list()
total_correct = 0
guessed_states = []

while game_is_on:
    answer_state = screen.textinput(title=f"{total_correct}/50 Guess the State", prompt="What's another State's name?").lower()
    if answer_state in all_states and answer_state not in guessed_states:
        found_state = state_data[state_data.state.str.lower() == answer_state]
        print(found_state.y)
        State(int(found_state.x), int(found_state.y), found_state.state.item())
        guessed_states.append(answer_state)
        total_correct += 1
        
    if total_correct == 50:
        game_is_on = False
        



screen.exitonclick()