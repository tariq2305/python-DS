import pgzrun
import random


HEIGHT = 500
WIDTH = 800

class Hero(Actor):
    def move(self):
        self.angle=10

        if keyboard.left:
            self.x -= 5
            self.angle=10
        elif keyboard.right:
            self.x +=5
            self.angle=-10
        elif keyboard.up:
            self.y-=5
            
        elif keyboard.down:
            self.y +=5
        else :
             self.angle = 0

    def warp(self):
        if self.x>WIDTH:
            self.x = 0
        if self.x < 0:
            self.x<WIDTH
        if self.y>HEIGTH:
                self.y <0
        if self.y< 0:
                    self.y = HEIGHT


class Ship(Actor):
    def track(self,player,speed =1):
        if player.x>self.x :
            self.x+= speed
        elif player.x<self.x:
            self.x-=speed
        if player.y>self.y:
            self.y+=speed
        elif player.y<self.y:
            self.y-=speed

p = Hero('image1',(100,100))
s= Ship('ship',(600,100))     #position,size
b= Rect((300 , 100),(32,32))
e=Ship('alien',(300,300))
def draw():
    screen.fill('black')
    p.draw()
    s.draw() 
    e.draw()##to draw something in the  game or program
    screen.draw.filled_rect(b,'orange')
def update():
    p.move()
    s.track(p,4)
    e.track(p,3)

pgzrun.go()