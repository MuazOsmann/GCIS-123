#Turtle 3
import turtle
import math

def Rectangle(Height, Width, PEN, FILL):
    turtle.begin_fill()
    turtle.fillcolor(FILL)
    turtle.pencolor(PEN)
    turtle.forward(Width)
    turtle.left(90)
    turtle.forward(Height)
    turtle.left(90)
    turtle.forward(Width)
    turtle.left(90)
    turtle.forward(Height)
    turtle.setheading(0)
    turtle.end_fill()
    print(turtle.ycor(), turtle.xcor())
    print(turtle.pencolor(), turtle.fillcolor())



def main():
    H = int(input("Please Inser the HEight : "))
    W = int(input("Please insert the Width : "))
    F = str(input("Please inset the fill color : "))
    P = str(input("Please insert the Pen color : "))
    Rectangle(H, W, P, F)
    print("Height : ", H, "Width : ", W )
    
main()
input("Please wait ...")