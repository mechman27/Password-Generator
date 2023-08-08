# from turtle import Turtle, Screen


# timmy = Turtle() 
# print(timmy)

# timmy.shape("square")
# timmy.color("blue")
# for i in range(20):
#     if i % 3: 
#         timmy.forward(200)
#         timmy.right(90)
#     if i == 10: 
#         timmy.forward(300)
#         timmy.right(90)
#     else:
#         timmy.forward(100)
#         timmy.right(90)


# my_screen = Screen()

# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()

pokemon = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander"]
types = ["Grass", "Grass", "Grass", "Fire"]

table.add_column("Pokemon Name", ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander"])
table.add_column("Type", ["Grass", "Grass", "Grass", "Fire"])

print(table)