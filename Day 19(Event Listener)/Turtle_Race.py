import turtle
import random

s = turtle.Screen()
y_coord = -100
s.setup(width=500, height=400)
user_bet = s.textinput(title="Make your Bet", prompt="Which Turtle will win the race: Enter a color").lower()
all_turtles = []


def creation_start():
    y_coord = -150
    list_position = 0
    color_list = ["red", "green", "blue", "purple", "orange", "yellow"]

    for i in range(0, 6):
        new_turtle = turtle.Turtle(shape="turtle")
        new_turtle.color(color_list[list_position])
        new_turtle.penup()
        new_turtle.goto(-230, y_coord)
        y_coord += 50
        list_position += 1
        all_turtles.append(new_turtle)


    

creation_start()
if user_bet: 
    is_game_on = True
    while is_game_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                winning_turtle = turtle.pencolor()
                is_game_on = False
                if winning_turtle == user_bet:
                    print(f"You won! The {winning_turtle} turtle was the winner")
                else:
                    print(f"You lost! The {winning_turtle} turtle was the winner")
            else:
                turtle.forward(random.randint(0, 10))
s.exitonclick()
