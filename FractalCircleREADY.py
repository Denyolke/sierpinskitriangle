import turtle
import math
import random

#constants
turtle.bgcolor("black")
turtle.speed(300)
turtle.pencolor("white")

#variables
#pos1
x1 = 259.81
y1 = 150.00

#pos2
x2 = -259.81
y2 = 150.00

#pos3
x3 = 0.00
y3 = -300.00



def draw_dot():
    turtle.penup()
    turtle.dot(3, "white")

def draw_red_dot():
    turtle.penup()
    turtle.dot(5, "red")


def draw_circle(radius):
    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()
    turtle.circle(radius)


def draw_triangle(radius):
    side_length = 2 * radius * math.sin(math.pi / 3)
    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()
    turtle.setheading(60)
    for i in range(3):
        turtle.penup()
        turtle.forward(side_length)
        turtle.left(120)
        draw_red_dot()
        global pos1,pos2,pos3
        if i == 0:
            pos1 = turtle.position()
        elif i == 1:
            pos2 = turtle.position()
        elif i == 2:
            pos3 = turtle.position()

def draw_line():
    global start
    starterx = 70
    startery = 50
    turtle.penup()
    turtle.goto(starterx, startery)
   # turtle.pendown()
    x = 0
    
    while x != 3000:
        start = random.randint(1, 3)
        if start == 1:
            turtle.goto(x1, y1)
            medianx = (starterx+x1)/2
            mediany = (startery+y1)/2
            turtle.goto(medianx,mediany)
            draw_dot()
            starterx = medianx
            startery = mediany
            
        elif start == 2:
            turtle.goto(x2, y2)
            medianx = (starterx+x2)/2
            mediany = (startery+y2)/2
            turtle.goto(medianx,mediany)
            draw_dot()
            starterx = medianx
            startery = mediany
        elif start == 3:
            turtle.goto(x3, y3)
            medianx = (starterx+x3)/2
            mediany = (startery+y3)/2
            turtle.goto(medianx,mediany)
            draw_dot()
            starterx = medianx
            startery = mediany
        x += 1
        #print(x)



def main():
    radius = 300
    draw_circle(radius)
    draw_triangle(radius)
    draw_line()
   

    turtle.hideturtle()
    turtle.done()
    

if __name__ == "__main__":
    main()