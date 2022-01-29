from turtle import *
from random import *
from math import *
from time import sleep

jimmy = Turtle()

def draw_reg_poly(name, sides, side_length, colour, text_colour):
    angle = 360/sides
    name.color(colour)
    name.begin_fill()
    for i in range(sides):
        name.forward(side_length)
        name.right(angle)
    name.end_fill()
    # if text_colour is 0 don't print the number of sides and length in the poly
    if text_colour != 0:
        name.color(text_colour)
        radius=side_length/(2*sin(radians(180/sides)))
        x = name.xcor() + side_length/2
        y = name.ycor() - radius
        name.goto(x, y-side_length/2)
        name.write(str(sides)+" "+str(side_length), font=("Arial", int(side_length/2), "normal"), align="center")

# function to pick a random colour from the web range: 0x000000 to 0xffffff
def get_random_web_color():
    colors=[]
    for col in range(3):
        colors.append(randint(0, 255))
    hex_color = f"#{colors[0]:02x}{colors[1]:02x}{colors[2]:02x}"
    return hex_color


jimmy.hideturtle()
jimmy.penup()
jimmy.speed(0) # fast speed

while True:
    for i in range(3, 10, 1):
        jimmy.goto(randint(-500, 500), randint(-400, 400))
        draw_reg_poly(jimmy, i, randint(25, 75), get_random_web_color(), 0)

    sleep(3)
    jimmy.clear()
