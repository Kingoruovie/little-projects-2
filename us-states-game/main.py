import turtle
import pandas as pd

# screen codes setup so to fit picture size
screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")

# The pen that writes names of states written correctly
state_writer = turtle.Turtle()
state_writer.hideturtle()
state_writer.penup()
state_writer.color("black")

# Collecting data from csv file using panda and converting to a dictionary to loop through
states_data = pd.read_csv("50_states.csv")
states = states_data.state.to_list()
x_coordinates = states_data.x.to_list()
y_coordinates = states_data.y.to_list()
dict_of_states = {}
for i in range(50):
    dict_of_states[states[i]] = (x_coordinates[i], y_coordinates[i])

# Loop to enhance continuous listing of states until all states are listed correctly
game_is_on_trail_count = 50
number_of_guessed_state = 0
list_of_guessed_states = []
game_is_on = True
while game_is_on:
    state_guessed = screen.textinput(title=f"{number_of_guessed_state}/50 guessed correctly",
                                     prompt="Name the states in US: ").title()
    if state_guessed in dict_of_states:
        list_of_guessed_states.append(state_guessed)
        state_writer.goto(dict_of_states[state_guessed])
        state_writer.write(arg=state_guessed, align="center", font=("Arial", 10, "italic"))
        game_is_on_trail_count -= 1
        number_of_guessed_state += 1
        if game_is_on_trail_count == 0:
            game_is_on = False
            state_writer.write(arg="SPECTACULAR", align="center", font=("Verdana", 50, "bold"))
    if state_guessed == "Exit":
        states_missed = [state for state in states if state not in list_of_guessed_states]
        for state in states:
            if state not in list_of_guessed_states:
                state_writer.color("red")
                state_writer.goto(dict_of_states[state])
                state_writer.write(arg=state, align="center", font=("Arial", 10, "bold"))
                state_missed_data = pd.Series(states_missed)
                state_missed_data.to_csv("state_missed.csv")
        game_is_on = False

screen.exitonclick()