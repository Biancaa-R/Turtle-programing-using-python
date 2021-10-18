#Program for working with turtle programing
#Turtle library is preinstalled

from turtle import*

bgcolor('black')
pencolor('yellow')
width(20)
penup()
goto(160,-100)
pendown()

left(90)
for i in range(4):
    forward(250)
    circle(34,90)

penup()
goto(85,30)
pencolor("fuchsia")
pendown()
circle(80,360)
penup()
goto(110,130)
pencolor("cyan")
pendown()
circle(7,360)
penup()

goto(130,260)
pencolor("light blue")
pendown()
left(90)
for i in range(6):
    forward(260)
    circle(33,60)
penup()

goto(3,7)
pencolor("beige")
pendown()
left(90)
forward(20)
right(180)
forward(40)
left(180)
forward(20)
right(90)
forward(20)
left(180)
forward(40)

penup()
#end
