
from pygame import *
from math import *
init()

RED=(255,0,0)

width,height=750,448

screen=display.set_mode((width,height))
black=(0,0,0)
back1=image.load('level1.gif')
back1a2=image.load('level1a2.gif')
#back2=image.load('level2.bmp')
#back3=image.load('level3.bmp')
back=back1

ROW=2
COL=3
jumpSpeed=-20
GROUND=628
bottom=GROUND
offset=0

Mario=Rect(690,535,50,93)
MarioList=[690,535,0,0]
V=[0,0,bottom,690]

gravity=1.5
X=0
Y=1
BOT=2
screenX=3


        #Green Pipes
objects=[Rect(1006+400,528,85,95),Rect(888+1020,477,83,146),Rect(1067+1240,427,85,196),Rect(937+1920,427,85,197),Rect(1018+7140,527,83,98),Rect(1038+7920,528,83,96)\
 #Floating Bricks
,Rect(999,425,50,50),Rect(958+140,425,50,50),Rect(1058+140,425,50,50),Rect(940+2260,377,50,50),Rect(750+3100,425,50,50),Rect(848+3100,425,50,50),Rect(599+3400,225,400,50),Rect(770+3780,255,150,50),Rect(920+3780,425,50,50),Rect(960+4040,425,100,50),Rect(420+5480,425,50,50),Rect(570+5480,225,150,50),Rect(920+5480,225,50,50),Rect(1070+5480,225,50,50),Rect(970+5480,425,100,50),Rect(880+7520,425,100,50),Rect(1030+7520,425,50,50)]

object_enter=[Rect(473+2400,420,44,12),Rect(953+7220,523,47,11)]



#------------------------------------------------------------------------

def addPics(name,start,end):

    mypics=[]
    for i in range(start,end+1):
        mypics.append(image.load("images/%s%03d.png" %(name,i)))
    
    return mypics

pics=[]  #2d list (4 rows 6 columns) (1-st column is the "idle" frame)
pics.append(addPics("Mario",1,6))  #RIGHT (001-006)
pics.append(addPics("Mario",7,12)) #DOWN  (007-012)
pics.append(addPics("Mario",13,18))#UP    (013-018)
pics.append(addPics("Mario",19,24))#LEFT  (019-024)

#------------------------------------------------------------------------

def objectCollide(objects,x,y):
    MarioRect=Rect(x,y,50,93)
    return MarioRect.collidelist(objects)

#------------------------------------------------------------------------

def drawGrid(x,y):
    for i in range(x/16):
        draw.line(screen,black,(0,16*i),(6765,16*i),1)
    for i in range(y):
        draw.line(screen,black,(16*i,0),(16*i,6765),1)









def drawScene(player,screen,objects,back):
    
    offset=V[screenX]-player[X]
    screen.blit(back,(offset,0))
    #draw.rect(screen,RED,(V[screenX],player[1],50,93))
    #draw.rect(screen,(0,255,0),(999+offset,425,50,50))
    for Object in objects:
        Object=Object.move(offset,0)
        
    display.flip()
    #print(V,MarioList)

#------------------------------------------------------------------------

def drawPlayer(player,picList):
    row=player[ROW]         #get the "row" number (0-3)
    col=int(player[COL])  #get the "col" (frame number) (0-5)
    pic=picList[row][col] #getting the picture we need (1 of the 24 pictures)
    screen.blit(pic,([V[screenX],player[Y]]))
    display.flip()

#------------------------------------------------------------------------
#------------------------------------------------------------------------

def move(player):
    keys=key.get_pressed()
    if keys[K_SPACE] and player[Y] + 93 == V[BOT] and V[Y] == 0:
        V[Y] = jumpSpeed # player must be sitting steady on a platform or the ground in order to jump
        
    if objectCollide(objects,player[X],player[Y]-2)!=-1:
            V[Y]=5
    if objectCollide(object_enter,player[X],player[Y])!=-1:
            back=back2
    if keys[K_LEFT] and player[X]>20 and objectCollide(objects,player[X]-21,player[Y])==-1:
        V[X] = -20
        player[ROW]=3
        if V[screenX]>200:
            V[screenX]-=20

    elif keys[K_RIGHT] and player[X]<10575 and objectCollide(objects,player[X]+21,player[Y])==-1:
        V[X] = 20
        player[ROW]=0
        if V[screenX]<940:
            V[screenX]+=20

    else:
        V[X]=0
        player[COL]=0
        player[COL]-=0.4

    player[COL]+=0.4

    if player[COL]>=len(pics[ROW]):
        player[COL]=1
    print(player[X],player[Y])   
    player[X] += V[X]
    V[Y] += gravity

#------------------------------------------------------------------------


#------------------------------------------------------------------------
                    
def check(player,plats):
    
    for Object in objects:
        if player[X]+50>Object[X] and player[X]<Object[X]+Object[3] and player[Y]+93<=Object[Y] and player[Y]+93+V[Y]>Object[Y]:
            V[BOT] = Object[Y]
            player[Y] = V[BOT] - 93
            V[Y] =0
        
    player[Y] += V[Y]
    if player[Y]+93 >= GROUND:# if player attempts to fall below the ground
        V[BOT] = GROUND
        player[Y] = GROUND - 93
        V[Y] = 0


#------------------------------------------------------------------------


running=True
myClock=time.Clock()
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
                
    #mx,my=mouse.get_pos()
    #move(MarioList)
    #check(MarioList,objects)
    #drawScene(MarioList,screen,objects,back)
    screen.blit(back,(-6080,0))
    display.flip()
    #drawPlayer(MarioList,pics)
    drawGrid(6765,448)
    display.flip()
    myClock.tick(60)
     
quit()

