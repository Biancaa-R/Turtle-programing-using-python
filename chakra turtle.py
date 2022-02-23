from turtle import *
def draw_squares():
    for i in range(0,5):
        forward(300)
        right(90)

def draw_smallsquares():
    for i in range(0,5):
        forward(150)
        right(90)        

def chakra():
    bgcolor('black')
    pencolor('yellow')
    width(2)
    penup()
    goto(160,-80)
    pendown()
    speed(7)
    
    for i in range(0,12):
        draw_squares()
        right(10)
    penup()    
    goto(3,7)
    pendown()
    pencolor("fuchsia")
    for i in range(0,12):
        draw_smallsquares()
        right(10)
    penup()
    pencolor("cyan")
    goto(150,15)
    pendown()
    for i in range(0,12):
        draw_squares()
        right(10)
    penup()    
   
chakra()
