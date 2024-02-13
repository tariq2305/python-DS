from turtle import *
speed('fastest')
pencolor('red')
pensize(5)
for i in range(8):
    fd(120)
    lt(45)
    write(f'n={i}',font=("calibri",16))


hideturtle()
mainloop()