"""
Uses two Turtle objects to draw on the screen
"""
from turtle import *
# Part 1
t1 = Turtle()
t2 = Turtle()
t1.pencolor('red')
t2.pencolor('blue')
t2.left(90)
t1.forward(100)
t2.forward(50)
t2 = t1
t2.right(45)
t2.forward(50)
done()
