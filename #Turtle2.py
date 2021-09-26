#Turtle2
import turtle
import math
def TrangleofTurtle():
    turtle.begin_fill()
    turtle.fillcolor("yellow")
    turtle.forward(100) # draw base
    
    turtle.left(120)
    turtle.forward(100)
 
    turtle.left(120)
    turtle.forward(100)
    turtle.end_fill()
    turtle.setheading(0)
    print("Y Coordiante : ", turtle.ycor(),"X Coordinate : ", turtle.xcor())
    print("Pen color : ", turtle.pencolor(),"Fill Color : ", turtle.fillcolor())

def BaseofTriangle(BaseSize):
    highet = math.sqrt (BaseSize**2-((BaseSize/2)**2))
    print("The size of the base of the triangle = ", str(BaseSize))

def main():
    TrangleofTurtle()
    base = int(input("please enter a value for the base: "))
    BaseofTriangle(base)

main()
    
