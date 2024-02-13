from turtle import *

pencolor('yellow')
bgcolor('black')

for i in range (6):
    fd(150)
    lt(360/6)
    
    
    for i  in range(6):
         fd(75)
         lt(360/6)
       
    dot(10)

hideturtle()
mainloop()