# from turtle import Turtle, Screen
# import random

# def random_color():
#     r = int(random.randint(0, 255))
#     g = int(random.randint(0, 255))
#     b = int(random.randint(0, 255))
#     return (r, g, b)

# screen = Screen()
# t = Turtle()
# screen.colormode(255)
# direction = ["left", "right", "forward"]
# t.speed(10)
# t.pensize(10)
# for _ in range(20):
#     new_direction = random.choice(direction)
#     t.color(random_color())
#     if new_direction == "left":
#         t.left(90)
#         t.forward(10)
#     elif new_direction == "right":
#         t.right(90)
#         t.forward(10)
#     else:
#         t.forward(10)

# screen.exitonclick()
"""Above is my first attempt to write a program that makes a turtle move 
in a random direction. """

import turtle as t
import random

def random_color():
    r = int(random.randint(0, 255))
    g = int(random.randint(0, 255))
    b = int(random.randint(0, 255))
    return (r, g, b)

screen = t.Screen()

t.colormode(255)
direction = [0, 90, 180, 270]
t.speed(25)
t.pensize(10)
for _ in range(200):
    new_direction = random.choice(direction)
    t.pencolor((random_color()))
    t.forward(20)
    t.setheading(new_direction)

screen.exitonclick()


