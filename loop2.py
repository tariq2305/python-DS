from turtle import *

speed ('fastest')
pensize(10) ##size of the length

s=0
while s<250:
    fd(50+s) ##forward movement
    rt(60) ##right move
    write(s)
    dot(20)
    s+= 5

hideturtle()
mainloop()