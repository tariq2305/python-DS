import pgzrun
import random

class Hero(Actor):
        def move(self):
                if keyword.left:
                        self.x -= 5
                elif keyword.right:
                        self.x +=5
                elif keyword.up:
                        self.y-=5
                elif keyword.down:
                        self.y +=5

              

HEIGHT = 500
WIDTH = 800
p = Hero('image1',(100,100))
b= Rect((300 , 100),(50,50))     #position,size
def draw():
        screen.fill('white')
        p.draw()
        screen.draw.filled_rect(b,'orange')
def update():
        p.move()
        

pgzrun.go()