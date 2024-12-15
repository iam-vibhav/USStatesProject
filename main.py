import pandas
import turtle as t

us_states = pandas.read_csv("50_states.csv")

states_dict = {}

for _, row in us_states.iterrows():
    state, x, y = row
    states_dict[state] = (x,y)


screen = t.Screen()
screen.title("US States Quiz Game")
image = "blank_states_img.gif"
screen.addshape(image)
us_map = t.Turtle()
us_map.shape(image)

points = 0

correct_state = t.Turtle()
correct_state.penup()
correct_state.hideturtle()

while points <= 50:
    if points == 0:
        state = screen.textinput(f"{points}/50 States Correct", "Guess a State")
        if state.title() in states_dict.keys():
            correct_state.goto(states_dict[state.title()])
            correct_state.write(state.title())
            del states_dict[state.title()]
            points += 1
    else:
        state = screen.textinput(f"{points}/50 States Correct", "Guess another State")
        if state.title() in states_dict.keys():
            correct_state.goto(states_dict[state.title()])
            correct_state.write(state.title())
            del states_dict[state.title()]
            points += 1

screen.exitonclick()

