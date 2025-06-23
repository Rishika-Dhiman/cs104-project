import pygame
import random
import parameters as p
import math

class Bird:
    def __init__(self,name,mass,images,block,number,dim):
        self.name=name
        self.mass=mass
        self.images=images
        self.block=block
        self.number=number
        self.dim=dim
        self.edmg=55
        self.dmg=35
        self.x_speed=0
        self.y_speed=0
    def getDamage(self,type):
        if self.block==type:
            return self.edmg
        else:
            return self.dmg

red=Bird('red',13,['Images/red1.png','Images/red2.png','Images/red3.png'],'all',1,[63,60])
chuck=Bird('chuck',15,['Images/chuck1.png','Images/chuck2.png','Images/chuck3.png'],'wood',2,[78,71])
blues=Bird('blues',10,['Images/blues1.png','Images/blues2.png','Images/blues3.png'],'glass',3,[61,61])
bomb=Bird('bomb',25,['Images/bomb1.png','Images/bomb2.png','Images/bomb3.png'],'stone',4,[65,98])

birds=[red,chuck,blues,bomb]

def generateBird(player):
    global birds
    b=random.choice(birds)
    i=Bird(b.name,b.mass,b.images,b.block,b.number,b.dim)
    bird_rect=[]
    bird=[]
    bird.append(i)
    bird_surface=pygame.image.load(i.images[0])
    bird_surface=pygame.transform.scale(bird_surface,((i.dim[0])*p.ratio,(i.dim[1])*p.ratio))
    if player==1:
        bird_rect.append(bird_surface.get_rect(center=(p.sling1[0],p.sling1[1])))
    else:
        bird_surface=pygame.transform.flip(bird_surface,True,False)
        bird_rect.append(bird_surface.get_rect(center=(p.size[0]-p.sling1[0],p.sling1[1])))
    return bird,bird_surface,bird_rect

def getSpeed(player,bird,mouse_x,mouse_y):
    dist_sling=0
    dirtheta=0
    if player==1:
        dist_sling=math.dist((mouse_x,mouse_y),(p.sling1[0],p.sling1[1]))
        dirtheta=math.atan2(p.sling1[1]-mouse_y,p.sling1[0]-mouse_x)
    else:
        dist_sling=math.dist((mouse_x,mouse_y),(p.sling2[0],p.sling2[1]))
        dirtheta=math.atan2(p.sling2[1]-mouse_y,p.sling2[0]-mouse_x)

    mass=bird.mass
    vconst=math.sqrt(p.kstring/mass)
    speed=vconst*dist_sling
    return speed,dirtheta,dist_sling

def extraAbility(bird,bird_rects,bird_surface,player):
    if bird[0].name=='red':
        bird[0].y_speed+=3*abs(bird[0].y_speed)
        bird[0].x_speed*=0.8
    elif bird[0].name=='chuck':
        bird[0].edmg+=20
        bird[0].dmg+=20
        bird[0].x_speed*=2
        bird[0].y_speed*=2
    elif bird[0].name=='blues':
        bird[0].dim=[51,51]
        bird1=Bird('blue1',10,['Images/blues1.png','Images/blues2.png','Images/blues3.png'],'glass',3,[51,51])
        bird3=Bird('blue1',10,['Images/blues1.png','Images/blues2.png','Images/blues3.png'],'glass',3,[51,51])
        bird1.x_speed=bird[0].x_speed
        bird3.x_speed=bird[0].x_speed
        bird1.y_speed=bird[0].y_speed
        bird3.y_speed=bird[0].y_speed 
        bird.append(bird1)
        bird.append(bird3)
        bird_rects.append(bird_rects[0].move(0,-61))
        bird_rects.append(bird_rects[0].move(0,61))
        for i in range(len(bird)):
            bird[i].edmg-=20
            bird[i].dmg-=20
    else:
        bird[0].edmg=100
        bird[0].dmg=80
    bird_surface=pygame.image.load(bird[0].images[1])
    bird_surface=pygame.transform.scale(bird_surface,((bird[0].dim[0])*p.ratio,(bird[0].dim[1])*p.ratio))
    if player==2:
        bird_surface=pygame.transform.flip(bird_surface,True,False)
    return bird_surface

def projectileDots(x_speed,y_speed,g,x_pos,y_pos):
    dot_positions=[]
    for i in range(1,15):
        y_speed+=g
        x_pos=x_pos+x_speed
        y_pos=y_pos+y_speed
        if y_pos>=p.groundlevel:
            y_speed*=-p.e
        dot_positions.append((x_pos,y_pos))
    return dot_positions