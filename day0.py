from turtle import *



#we want to paint a house

#step 1: draw a spuare
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)






#end of square
#drawing a door

forward(120)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(55)
#end of door
#drawing a roof
penup()
goto(200,200)


pendown()

color("black")
right(135)
forward(140)
left(90)
forward(140)
#the end of the roof
#drawling a window
left(135)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

penup()
goto(200,200)
pendown()

forward(50)
left(90)
forward(50)
left(90)
forward(50)



exitonclick()