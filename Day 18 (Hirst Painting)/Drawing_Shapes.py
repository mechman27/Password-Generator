from turtle import Turtle, Screen
import random
def random_color():
    r = int(random.randint(0, 255))
    g = int(random.randint(0, 255))
    b = int(random.randint(0, 255))
    return (r, g, b)


def draw_shape(shape_sides):
        
    timmy.color(random_color())
    for i in range(shape_sides):
        timmy.forward(100)
        timmy.right(360/shape_sides)


screen = Screen()
timmy = Turtle()
timmy.shape("turtle")
screen.colormode(255)
for _ in range(8):
    draw_shape(timmy, _ + 3)
    

screen.exitonclick()
