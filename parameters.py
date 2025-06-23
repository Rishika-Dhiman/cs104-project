import numpy as np
size=1280,720
White=(255,255,255)
Black=(0,0,0)
Grey=(250,250,250)
Darkgrey=(70,70,70)
player1=''
player2=''
g=3000
d=2500
e=0.6
stringlen=100
kstring=2000
m=2
n=3
ratio=0.6

sling1=np.array([341,497])
sling2=np.array([1280-341,497])
groundlevel=620

score1=0
score2=0

mode=0
timelimit=60
wind=False
moving=False
motiondots=False
result=2

def setGrid(a,b):
    global m,n
    m=a
    n=b
    return

def setMode(m):
    global mode
    mode=m
    return

def setWind(w):
    global wind
    wind=w
    return

def setMoving(m):
    global moving
    moving=m
    return

def storeName(name1,name2):
    global player1,player2
    player1=name1
    player2=name2
    return

def updateScore(player,score):
    global score1,score2
    if player==1:
        score1+=score
    else:
        score2+=score
    return

def storeResult(r):
    global result
    result=r
    return

def setDifficulty(difficulty):
    global wind,moving,m,n,d,motiondots
    if difficulty==1:
        wind=False
        moving=False
        motiondots=True
        m=2
        n=2
    elif difficulty==2:
        wind=True
        d=1500
        moving=False
        motiondots=True
        m=2
        n=4
    elif difficulty==3:
        wind=True
        moving=True
        motiondots=False
        m=3
        n=4
    return