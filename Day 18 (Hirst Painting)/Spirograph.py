# import turtle as t
# import random

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)

# t.colormode(255)
# t.speed("fastest")
# for _ in range(100):
#     t.pencolor(random_color())
#     t.circle(100)
#     t.right(3.75)

# t.exitonclick()
"""This was my code for the first part of the assignment"""

import turtle as t
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

t.colormode(255)
t.speed("fastest")
def draw_spirograph(size_of_gap):

    for _ in range(int(360/size_of_gap)):
        t.pencolor(random_color())
        t.circle(100)
        t.setheading(t.heading()+size_of_gap)


draw_spirograph(int(input("What angle would you like to draw at? ")))

t.exitonclick()
