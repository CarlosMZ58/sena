import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(10000000000)
n = 100
h = 10 
for i in range (380):
    c= colorsys.hsv_to_rgb(h, 1, 0.8)
    h = h + 1/n
    t.color(c)
    t.forward(i*2)
    t.left(140)
    
turtle.done()