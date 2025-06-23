import pygame
import random
import parameters as p
from parameters import updateScore,storeResult

class Block:
    def __init__(self,type,imagelist,health):
        self.type=type
        self.imagelist=imagelist
        self.health=health
    def getImage(self):
        if self.health>75:
            return self.imagelist[0]
        elif self.health>50 and self.health<=75:
            return self.imagelist[1]
        elif self.health>25 and self.health<=50:
            return self.imagelist[2]
        elif self.health>0 and self.health<=25:
            return self.imagelist[3]

glassimgs=['Images/glass1.png', 'Images/glass2.png', 'Images/glass3.png', 'Images/glass4.png']
woodimgs=['Images/wood1.png', 'Images/wood2.png', 'Images/wood3.png', 'Images/wood4.png']
stoneimgs=['Images/stone1.png', 'Images/stone2.png', 'Images/stone3.png', 'Images/stone4.png']

glass1=Block('glass',glassimgs,100)
wood1=Block('wood',woodimgs,100)
stone1=Block('stone',stoneimgs,100)

blocks=[glass1,wood1,stone1]

def generateFortress(player):
    global blocks
    block_surfacelist=[]
    block_rectlist=[]
    x=1027
    y=593
    i=1
    if player==1:
        c=54
        x=1027
    else:
        c=-54
        x=p.size[0]-1027
    rblocks=[Block(b.type, b.imagelist, b.health) for b in random.choices(blocks, k=(p.m * p.n))]
    block_surfacelist=[[]for _ in range(p.m)]
    block_rectlist=[[] for _ in range(p.m)]
    blockslist=[[] for _ in range(p.m)]
    for i in range(0,p.m):
        for j in range(0,p.n):
            block_surface=pygame.image.load(rblocks[(p.n)*i+j].getImage())
            block_surface=pygame.transform.scale(block_surface,(54,54))
            block_surfacelist[i].append(block_surface)
            block_rect=block_surface.get_rect(center=(x,y))
            block_rectlist[i].append(block_rect)
            blockslist[i].append(rblocks[(p.n)*i+j])
            y-=54
        x+=c
        y+=54*p.n
    return block_surfacelist,block_rectlist,blockslist

def detectCollision(player,bird,bird_rect,block_rectlist,block_surfacelist,block_list,bird_surface):
    for i, block_rectcol in enumerate(block_rectlist):
        for j, block_rect in enumerate(block_rectcol):
            length=len(block_rectcol)
            if bird_rect.colliderect(block_rect):
                if abs(bird_rect.centerx-block_rect.centerx)<abs(bird_rect.centery-block_rect.centery) and j==length-1:
                    bird_rect.bottom=block_rect.top
                    bird.y_speed*=-0.5
                else:
                    if player==1:
                        bird_rect.right=block_rect.left
                    else:
                        bird_rect.left=block_rect.right
                    bird.x_speed*=-0.5
                damage=bird.getDamage(block_list[i][j].type)
                if block_list[i][j].health<damage:
                    damage=block_list[i][j].health
                updateScore(player,damage)
                block_list[i][j].health-=damage
                if bird.edmg-40>0:
                    bird.edmg-=40
                else:
                    bird.edmg=0
                if bird.dmg-20>0:
                    bird.dmg-=10
                else:
                    bird.dmg=0
                bird_surface=pygame.image.load(bird.images[2])
                bird_surface=pygame.transform.scale(bird_surface,((bird.dim[0])*p.ratio,(bird.dim[1])*p.ratio))
                if player==2:
                    bird_surface=pygame.transform.flip(bird_surface,True,False)
                if block_list[i][j].health>0:
                    block_surfacelist[i][j]=pygame.transform.scale(pygame.image.load(block_list[i][j].getImage()),(54,54))
                return bird_surface
    return bird_surface

def fallingBlocks(x,y,block_list,block_rectlist,falling):
    if falling:
        if len(block_list[x])==0 or len(block_list[x])<=y:
            falling=False
            return falling
        for j, block in enumerate(block_list[x]):
            if j>=y:
                if j==y and j!=0:
                    if block_rectlist[x][j].bottom>=block_rectlist[x][j-1].top:
                        falling=False
                        break
                elif j==0:
                    if block_rectlist[x][j].bottom>=p.groundlevel:
                        falling=False
                        break
                if falling:
                    block_rectlist[x][j].centery+=9
    return falling

def blockDestroyed(block_list,block_surfacelist,block_rectlist,falling,x,y):
    destroyed=False
    for i, block_col in enumerate(block_list):
        length=len(block_col)
        for j, block in enumerate(block_col):
            if block.health<=0:
                x=i
                y=j
                destroyed=True
                falling=True
                break
        if destroyed:
            break
    if destroyed:
            del block_list[x][y]
            del block_surfacelist[x][y]
            del block_rectlist[x][y]
    return falling,x,y

def moveFortress(blockrect_list,c,player,disp):
    for i, blockrect_col in enumerate(blockrect_list):
        for j, blockrect in enumerate(blockrect_col):    
            blockrect_list[i][j].centerx+=c
    disp+=c
    if player==1:
        if disp>=p.size[0]+27-(54*p.m)-1027 and c==9:
            c=-9
        if disp<=0 and c==-9:
            c=9
    else:
        if disp<=-27+54*p.m-p.size[0]+1027 and c==-9:
            c=9
        if disp>=0 and c==9:
            c=-9
    return c,disp

def gameEnd(player,generatebird,splayer):
    end=False
    if player==splayer and (p.score1==p.n*p.m*100 or p.score2==p.n*p.m*100) and generatebird:
        if p.score1==p.score2 and p.score1!=0:
            storeResult(2)
            end=True
        elif p.score1>p.score2:
            storeResult(0)
            end=True
        elif p.score2>p.score1:
            storeResult(1)
            end=True
        else:
            end=False
    return end