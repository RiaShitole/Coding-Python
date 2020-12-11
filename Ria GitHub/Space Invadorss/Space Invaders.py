import random
import pygame
from pygame.locals import*
pygame.init()
screen=(pygame.display.set_mode((1000,800)))
pygame.display.set_caption('ria')
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(250,250,250)
yellow=(255,255,0)
black=(0,0,0)
orange=(252, 176, 10)
x=100
y=70
GreenAlien=pygame.image.load("Green Alien.png")
GreenAlien=pygame.transform.scale(GreenAlien,(30,30))
YellowAlien=pygame.image.load("Yellow Alien.png")
YellowAlien=pygame.transform.scale(YellowAlien,(30,30))
OrangeAlien=pygame.image.load("Orange Alien.png")
OrangeAlien=pygame.transform.scale(OrangeAlien,(30,30))
RedAlien=pygame.image.load("Red Alien.png")
RedAlien=pygame.transform.scale(RedAlien,(30,30))
allaliens=[]

class Alien():
    def __init__(self,x,y,color,image):
        self.x=x
        self.y=y
        self.color=color
        self.image=image
    def draw(self):
        screen.blit(self.image,(self.x,self.y))
        
##        pygame.draw.circle(screen,self.color,(self.x,self.y),20,0)

for mult in range(1,13,1):
    newalien=Alien(x,y,green,GreenAlien)
    x=x+70
    allaliens.append(newalien)

y=y+70
x=100
for sec in range(1,13,1):
    newalien=Alien(x,y,yellow,YellowAlien)
    allaliens.append(newalien)
    x=x+70
    

y=y+70
x=100
for sen in range(1,13,1):
    newalien=Alien(x,y,orange,OrangeAlien)
    allaliens.append(newalien)
    x=x+70
    
y=y+70
x=100
for sen in range(1,13,1):
    newalien=Alien(x,y,red,RedAlien)
    allaliens.append(newalien)
    x=x+70
while 1>0:
    pygame.display.update()
    screen.fill(black)
    for newalien in allaliens:
        newalien.draw()

    for event in pygame.event.get():
        if event.type==QUIT:#allow to quit the game
           
            pygame.quit()
            exit()

       
