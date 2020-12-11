import pygame#imports pygame
from pygame.locals import*#makes sure pygame is dowloaded
import random#importing random modul
pygame.init()#It starts the pygame engine
screen=(pygame.display.set_mode((1000,750)))#Here we are Creating the Screen
pygame.display.set_caption('ria')#sets name
Red=(255,0,0)#is a color varible
green=(0,255,0)#is a color varible
Blue=(0,0,255)#is a color varible
white=(255,255,255)#is a color varible
yellow=(255,255,0)#is a color varible
black=(0,0,0)#is a color varible
allballoons=[]#is a list
score=0#is the score on how many balloons u have popped
alletters=['a','b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n','p','q','r','s','t', 'v', 'w','x', 'y', 'z']#list of letters   
class Balloon:#making class
    def __init__(self,x,y,letter):#making funtion
        self.x=x#defining attipute
        self.y=y#defining attipute
        self.letter=letter#defining attipute
    def Draw(self):#making funtion
##        pygame.draw.circle(screen,Red,(self.x,self.y),30)
        screen.blit(balloonimage,(self.x,self.y))#adding the balloon image
    def move(self):#making a funtion
        self.y=self.y+1#adding y to make the balloon go down
        if self.y==750:#if continone
            self.y=0#if y=0
    def displayletter(self):#making funtion
        show_text(self.letter,self.x+25,self.y+20,white)#showing text
for a in range(1,11,1):#Makes a For loop       
    BalloonObject=Balloon(random.randint(0,1000),random.randint(0,750),random.choice(alletters))#making the balloon Object
    allballoons.append(BalloonObject)#Adding balloonObject to the class
def show_text(msg,x,y,color):#making the funtion show text
    
    fontobj=pygame.font.SysFont("Monotype Corsiva.ttf",50)#chooses the font 
    msgobj=fontobj.render(msg,True,color)#making an object
    screen.blit(msgobj,(x,y))#Adding the image
    
balloonimage=pygame.image.load('Balloon-removebg-preview.png')#loading the image
balloonimage=pygame.transform.scale(balloonimage,(80,80))#Making it a diffrent size
while 1>0:#makes whatever is in it goes forever
    
    pygame.display.update()#Displaying the screen
    screen.fill(black)#makes the screen black
    show_text(str(score),900,0,white)#makes the score a String
    for eachballoon in allballoons:#Starts the for loop
        eachballoon.Draw()#drawing the balloons
        eachballoon.displayletter()#makes sure that the balloons Apear(by updating the Screen)
        eachballoon.move()#moves the balloon
        
    for event in pygame.event.get():#starts the event loop
        if event.type==KEYDOWN:#if loop for if any key is pressed
            for eachballoon in allballoons:#Starts another for loop
                if chr(event.key)==eachballoon.letter:#turns the letters into ints
                    print('Just Found A MATCH')#prints if the letter matched
                    allballoons.remove(eachballoon)#removes letter/balloon if letter same is pressed
                    BalloonObject=Balloon(random.randint(0,1000),random.randint(0,750),random.choice(alletters))#MAKES THE Autual ballloon shape
                    allballoons.append(BalloonObject)#adds a new balloon if one disapears
                    score=score+1#adds score by 1 if we pop a BALLOON
                    pygame.display.update()#displays update so we can see the new balloons and the ones that POPPED
                    
                
            print(chr(event.key))#Prints the score 




    for event in pygame.event.get():#starts the  event for loop
        if event.type==QUIT:#if red button is pressed
            pygame.quit()#pygame should QUIT
            exit()#EXIT the program and BACK to the CODE
    if score==100 or score>100:#IF the score is 100 for over 100 
        print('Congrats!! You Won!! Restart To Play Again!')#print the congrats page
        pygame.display.update()#display the screen so u can see the score.
        exit()#finally exit EVERYtHING

