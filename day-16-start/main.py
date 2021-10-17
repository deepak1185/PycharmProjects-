#
# import another_module
# print(another_module.another_variable)
#
# import turtle
# from turtle import Turtle, Screen
# import prettytable
# timmy = Turtle()
#
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
#
#
# my_screen = Screen()
#
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
print(table)
#x = PrettyTable()
table.add_column("My Name", ["Pikachu", "charmandle", "squirmendle"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
# table.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
# table.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
# table.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769])
# table.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])

print(table)













