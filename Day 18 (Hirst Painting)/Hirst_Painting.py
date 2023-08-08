#import colorgram

#colors = colorgram.extract("Intermediate/Day 18 (Hirst Painting)/Hirst.jpg", 30)  

# for i in colors:
#     if 
#     color_list.append((i.rgb[0], i.rgb[1], i.rgb[2]))

# print(color_list)
################################################################
#Extracted the color_list list using the colorgram library
import turtle as t
import random as r

t.colormode(255)
color_list = [(192, 166, 113), (138, 166, 190), (55, 102, 140), (140, 91, 50), (11, 22, 53), (222, 207, 122), (183, 155, 40), (60, 22, 11), (182, 144, 165), (142, 177, 152), (72, 117, 80), (58, 14, 25), (126, 79, 102), (131, 29, 15), (16, 40, 26), (22, 53, 128), (177, 188, 215), (163, 105, 138), (114, 32, 48), (98, 150, 98), (95, 122, 174), (210, 179, 199), (178, 102, 91), (25, 90, 63), (73, 151, 165), (173, 205, 180)]
t.penup()
t.hideturtle()
t.speed("fastest")

t.setheading(225)
t.forward(400)
t.setheading(0)
Number_of_dots = 100

for dots in range(1, Number_of_dots + 1):
    t.dot(20, r.choice(color_list))
    t.forward(50)
    if dots % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


t.exitonclick()