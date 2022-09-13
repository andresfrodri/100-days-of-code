"""import turtle

ham = turtle.Turtle()
ham.shape("turtle")
ham.color('DarkGreen')


my_screen = turtle.Screen()

ham.forward(100)

my_screen.exitonclick()


"""

import prettytable

table = prettytable.PrettyTable()
print(table)
print("------------")
table.add_column("Pokémon",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
print(table)

table.align="l"
print(table)