import time
import pygame,sys,random
from pygame.locals import *
import math
from pygame import mixer

pygame.init()
screenlengthx=600
screenlengthy=600
screen=pygame.display.set_mode((screenlengthx,screenlengthy))

intro_bg=pygame.image.load('bg1.jpg')
intro_bg=pygame.transform.scale(intro_bg,(screenlengthx,screenlengthy))

ox=20
oy=screenlengthy
r=20;
incr=0
axlr=-1;
high=20
gapx=250
gapy=200;
barw=70
bars=[]
sp=screenlengthx*2
store=[]
cb=(255,0,0)
for i in range(3):bars.append([sp+(i*(gapx+barw)),random.randint(gapy,screenlengthy-gapy)])
def text_objects(text, font):
    textSurfac = font.render(text, True, (255,255,255))
    return textSurfac, textSurfac.get_rect()
 

def button(text,x,y,w,h,c1,c2,ask):
    mice=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if((x+w>mice[0]>x) and (y+h>mice[1]>y)):
        
        if click[0]==1:
            #=mixer.Sound('laser.wav')
            #clm.play()
            return ask
        pygame.draw.rect(screen,c2,(x,y,w,h))
    else:pygame.draw.rect(screen,c1,(x,y,w,h))
    buttontext=pygame.font.Font('freesansbold.ttf',40)
    textsurf,textRect=text_objects(text,buttontext)
    textRect.center=( (x+(w/2)), (y+(h/2)) )
    screen.blit(textsurf,textRect)
print(bars)
running=False
intro=True
while intro:
    screen.fill((66, 236, 245))
    screen.blit(intro_bg,(0,0))
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.quit()
        
        action= button("PLAY",220,250,200,60,(75, 97, 70),(45, 224, 0),"start")       
        if (action=="start"):
            running=True
            intro=False
        pygame.display.update()
        
        
while running:
    screen.fill((0,0,0))
    #screen.blit(sg2,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
                pygame.quit()
                sys.exit()
                running=False
        if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    running=False
        if event.type == KEYDOWN:
                if event.key == K_SPACE :
                    incr=1
                    
    oy-=incr
    pygame.draw.circle(screen,cb,(int(ox+r),int(oy-r)),r)
    
    pygame.draw.line(screen,(0,255,0),((ox+2*r+2),screenlengthy),((ox+2*r+2),0),2)
    
    for i in range(3):
        pygame.draw.rect(screen,(255,255,255),(int(bars[i][0]),0,int(barw),int(bars[i][1])))
        pygame.draw.rect(screen,(255,255,255),(int(bars[i][0]),int(bars[i][1])+gapy,int(barw),screenlengthy-int(bars[i][1])-gapy))
        bars[i][0]-= 0.3
    
        if((int(bars[i][0])+barw)<0):
            bars[i]=[bars[(i+2)%3][0]+gapx,random.randint(gapy,screenlengthy-gapy)]
            store=[]
            cb=(255,0,0)
        if(int(bars[i][0])<(ox+2*r+2)):
            store=bars[i]
            

    if(oy<screenlengthy-2):
        if(incr>0):incr-=0.008
        else:incr-=0.002
    else:incr=0
    if(len(store)!=0):
        pygame.draw.line(screen,(251, 255, 0),(0,store[1]),(screenlengthx,store[1]),2)
        pygame.draw.line(screen,(251, 255, 0),(0,store[1]+gapy),(screenlengthx,store[1]+gapy),2)
        
        if((ox>=store[0]) and ((ox+2*r)<=store[0]+barw)):
            if((oy>=store[1]+gapy) or ((oy-2*r)<=store[1])):
                cb=(0,0,255)
                print(store[1],oy,store[1]+gapy)
    pygame.display.update()
      