import pandas as pd
import turtle

s = turtle.Screen()
s.title("U.S. States Game")
image = "Intermediate/Day 25/States Game/blank_states_img.gif"
s.addshape(image)
turtle.shape(image)
data = pd.read_csv("Intermediate/Day 25/States Game/50_states.csv")
states = data.state.to_list()
score = 0
total = len(states)
guessed_state = []

while score != total:
    answer_state = s.textinput(title = f"{len(guessed_state)}/{total}Guess the State", prompt = "Name a State:").title()
    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_state:
                missing_states.append(state)
        df = pd.DataFrame(missing_states)
        df.to_csv("Intermediate/Day 25/States Game/missing_states.csv")
        break
    if answer_state in states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

    

t.mainloop()