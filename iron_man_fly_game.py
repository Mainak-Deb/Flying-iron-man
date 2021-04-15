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

bg2=pygame.image.load('factory_bg_1.jpg')
bg2=pygame.transform.scale(bg2,(screenlengthx*4,screenlengthy))


ims=pygame.image.load('flying_iron_man-removebg-preview.png')
ims=pygame.transform.scale(ims,(80,80))


gameover_bg=pygame.image.load('bg4.jpg')
gameover_bg=pygame.transform.scale(gameover_bg,(screenlengthx,screenlengthy))


obtc=pygame.image.load('Screenshot__1391_-removebg-preview.png')

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
speed=5
bgx=0
cb=(255,0,0)
bgarr=[0,screenlengthx*4]
score=0;

obtc_r=pygame.transform.rotate(obtc,180)
fonts1=pygame.font.Font('freesansbold.ttf',40)


def obstacle(obtc,x,y,a,b):
    obtc=pygame.transform.scale(obtc,(a+100,410))
    screen.blit(obtc,(x-55,y-60))
def r_obstacle(img,x,y,a,b):
    img=pygame.transform.scale(img,(a+100,500))
    screen.blit(img,(x-55,b-425))


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
gameover=False

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
    #print(bgarr[0])
    mice=pygame.mouse.get_pos()
    # print(mice)
    screen.blit(bg2,(bgarr[0],0))
    screen.blit(bg2,(bgarr[1],0))
    if(bgarr[0]<(-1*(screenlengthx*4))):
        bgarr.pop(0)
        bgarr.append(screenlengthx*4)
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
                    
    oy-=incr*speed
    #pygame.draw.circle(screen,cb,(int(ox+r),int(oy-r)),r)
    ims_c=pygame.transform.rotate(ims,incr*50)
    screen.blit(ims_c,(ox-int(ims_c.get_width()/2)+25,oy-2*r-int(ims_c.get_height()/2)+10))
    
    #pygame.draw.line(screen,(0,255,0),((ox+2*r+2),screenlengthy),((ox+2*r+2),0),2)
    
    for i in range(3):
        # pygame.draw.rect(screen,(255,255,255),(int(bars[i][0]),0,int(barw),int(bars[i][1])))
        # pygame.draw.rect(screen,(255,255,255),(int(bars[i][0]),int(bars[i][1])+gapy,int(barw),screenlengthy-int(bars[i][1])-gapy))
        obstacle(obtc,int(bars[i][0]),int(bars[i][1])+gapy,int(barw),screenlengthy-int(bars[i][1])-gapy)
        r_obstacle(obtc_r,int(bars[i][0]),0,int(barw),int(bars[i][1]))
        bars[i][0]-= 0.3*speed
    
        if((int(bars[i][0])+barw)<0):
            bars[i]=[bars[(i+2)%3][0]+gapx,random.randint(int(gapy/2),screenlengthy-gapy)]
            store=[]
            score+=1
            cb=(255,0,0)
        if(int(bars[i][0])<(ox+2*r+2)):
            store=bars[i]
            

    if(oy<screenlengthy-2):
        if(incr>0):incr-=0.008*speed
        else:incr-=0.002*speed
    else:incr=0
    if(len(store)!=0):
        # pygame.draw.line(screen,(251, 255, 0),(0,store[1]),(screenlengthx,store[1]),2)
        # pygame.draw.line(screen,(251, 255, 0),(0,store[1]+gapy),(screenlengthx,store[1]+gapy),2)
        
        if((ox>=store[0]) and ((ox+2*r)<=store[0]+barw)):
            if((oy>=store[1]+gapy) or ((oy-2*r)<=store[1])):
                cb=(0,0,255)
                gameover=True
                running=False

                #print(store[1],oy,store[1]+gapy)
    
    bgarr[0]=bgarr[0]-1.5
    bgarr[1]=bgarr[1]-1.5
    g2=fonts1.render("Score: "+str(score),True,(235, 238, 242))
    screen.blit(g2,(screenlengthx-200,20))

    pygame.display.update()

while gameover:
    screen.fill((66, 236, 245))
    screen.blit(gameover_bg,(0,0))
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            gameover=False
    g3=fonts1.render("F**k off",True,(255, 247, 0))
    g4=fonts1.render("You are not eligable to ",True,(13, 255, 0))
    g5=fonts1.render("fly iron man suit",True,(13, 255, 0))
    g6=fonts1.render("Your Score: "+str(score),True,(255, 0, 72))
    screen.blit(g3,(200,20))
    screen.blit(g4,(70,300))
    screen.blit(g5,(120,400))
    screen.blit(g6,(150,500))
    pygame.display.update()
    
      