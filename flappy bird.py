import random
import pygame
from pygame.locals import*
pygame.init()
screen=(pygame.display.set_mode((600,600)))
pygame.display.set_caption('ria')
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(250,250,250)
yellow=(255,255,0)
birdx=300
birdy=300
xtop=400
ytop=0
toplen=200
xdown=400
score=0
birdonscreen=0
toppipe=0
bottompipe=0

ydown=500#because the legs of the bottom is 600 and the pole' lenght 200, 600-200=400
downlen=200
bird=pygame.image.load('bird2.png')
bird=pygame.transform.scale(bird,(50,50))
background=pygame.image.load('flappy background.jpg')
background=pygame.transform.scale(background,(600,600))
ydownlist=[300,400,500]

      
          
        
#hight of toppipe+ the hight of the gap=? the hight of the screen-?= the hight of the bottom pipe
       

while 1>0:
    pygame.display.update()
    screen.fill(white)
    screen.blit(background,(0,0))
    birdonscreen=screen.blit(bird,(birdx,birdy))
    birdy=birdy+1#makeing the bird go down
                
   
   #### pygame.draw.circle(screen,yellow,(birdx,birdy),45)#made the bird
    toppipe=pygame.draw.rect(screen,blue,(xtop,ytop,20,toplen))#made the top pipe
    bottompipe=pygame.draw.rect(screen,blue,(xdown,ydown,20,downlen))#made the down pipe
    xtop=xtop+-2#moveing the top pipe
    xdown=xdown-2#moved the down pipe
    if xdown==0:#checking if the down pipe went of the screen
        score=score+1
        xdown=600#making the down pipe come to the right side
    if xtop==0:##checking if the top pipe went of the screen
        ydown=random.choice(ydownlist)
        
        xtop=600
        
        
        
        
   
        
        
       
      
      
   
        
    if birdonscreen.colliderect(bottompipe):#if the bird hits the down pipe
        print('your score was',score)
        pygame.quit()
        exit()
    if birdonscreen.colliderect(toppipe):#if the bird hits the top pipe
        print('your score was',score)
        pygame.quit()
        exit()
    if birdy==600:# if the bird hits the bottom
        print('your score  was',score)
        exit()
    
    
        
    for event in pygame.event.get():
        
        if event.type==QUIT:#allow to quit the game
            print('your score was',score)
            pygame.quit()
            exit()
        if event.type==KEYDOWN:#if any key is pressed down
            if event.key==K_SPACE:#if space is pressed
                birdy=birdy+-30#moveing the bird up
                
                
