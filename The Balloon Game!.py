import pygame
from pygame.locals import*#
import random#importing random modul
pygame.init()#It starts the pygame engine
screen=(pygame.display.set_mode((1000,750)))#Here we are Creating the Screen
pygame.display.set_caption('ria')
Red=(255,0,0)
green=(0,255,0)
Blue=(0,0,255)
white=(255,255,255)
yellow=(255,255,0)
black=(0,0,0)
allballoons=[]
score=0
alletters=['a','b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n','p','q','r','s','t', 'v', 'w','x', 'y', 'z']   
class Balloon:
    def __init__(self,x,y,letter):
        self.x=x
        self.y=y
        self.letter=letter
    def Draw(self):
##        pygame.draw.circle(screen,Red,(self.x,self.y),30)
        screen.blit(balloonimage,(self.x,self.y))
    def move(self):
        self.y=self.y+1
        if self.y==750:
            self.y=0
    def displayletter(self):
        show_text(self.letter,self.x+25,self.y+20,white)
for a in range(1,11,1):       
    BalloonObject=Balloon(random.randint(0,1000),random.randint(0,750),random.choice(alletters))
    allballoons.append(BalloonObject)
def show_text(msg,x,y,color):
    
    fontobj=pygame.font.SysFont("Monotype Corsiva.ttf",50)
    msgobj=fontobj.render(msg,True,color)
    screen.blit(msgobj,(x,y))
    
balloonimage=pygame.image.load('Balloon-removebg-preview.png')
balloonimage=pygame.transform.scale(balloonimage,(80,80))
while 1>0:
    
    pygame.display.update()
    screen.fill(black)
    show_text(str(score),900,0,white)
    for eachballoon in allballoons:
        eachballoon.Draw()
        eachballoon.displayletter()
        eachballoon.move()
        
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            for eachballoon in allballoons:
                if chr(event.key)==eachballoon.letter:
                    print('Just Found A MATCH')
                    allballoons.remove(eachballoon)
                    BalloonObject=Balloon(random.randint(0,1000),random.randint(0,750),random.choice(alletters))
                    allballoons.append(BalloonObject)
                    score=score+1
                    pygame.display.update()
                    
                
            print(chr(event.key))




    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
    if score==100 or score>100:
        print('Congrats!! You Won!! Restart To Play Again!')
        pygame.display.update()
        exit()

