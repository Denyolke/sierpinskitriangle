import turtle
t = turtle.Turtle()

#constants
turtle.speed(0)
turtle.bgcolor("black")
t.pencolor("white")
t.fillcolor("white")



def drawTriangle():
    t.teleport(-150,-50)
    for i in range(3):
        t.forward(300)
        t.left(120)
    t.hideturtle()



def drawCircle():
    t.teleport(0,-150)
    t.circle(200)
    t.hideturtle()

def drawDot():
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    

def drawInDots():
    t.goto(0,-150)
    t.begin_fill()
    t.circle(10)
    t.end_fill()


drawCircle()
drawDot()
