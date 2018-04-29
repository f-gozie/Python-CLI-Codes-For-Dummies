""" Draws in the window a spiral surrounded with an octagon """

from turtle import *

def octogon(t, x, y, color):
    """ Draws with turtle t an octogon centered at (x, y) with specified color"""
    t.pencolor(color)
    t.penup()
    t.setposition(x, y)
    t.pendown()
    for i in range(8):
        t.forward(80)
        t.right(45)


def spiral(t, x, y, color):
    """
    Draws with turtle t a spiral centered at (x, y)
    with the specified color
    """
    distance = 0.2
    angle = 40
    t.pencolor(color)
    t.penup()
    t.setposition(x, y)
    t.pendown()
    for i in range(100):
        t.forward(distance)
        t.left(angle)
        distance += 0.5

t = Turtle()
octogon(t, -45, 100, 'red')
spiral(t, 0, 0, 'blue')
t.hideturtle()
done()