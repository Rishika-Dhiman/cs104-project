import pygame
import math
import random
import parameters as p
from parameters import storeResult
from bird import generateBird,getSpeed,extraAbility,projectileDots
from blocks import generateFortress,detectCollision,fallingBlocks,blockDestroyed,moveFortress,gameEnd

pygame.init()

def gameStart():
    running=True
    width=p.size[0]
    height=p.size[1]    
    screen=pygame.display.set_mode(p.size)
    pygame.display.set_caption('Angry Birds')
    clock=pygame.time.Clock()

    background=pygame.image.load('Images/background.jpg')
    background=pygame.transform.scale(background, (p.size))
    logo=pygame.image.load('Images/Angry_Birds_logo.png')
    logo=pygame.transform.smoothscale(logo,(500,113.33))
#generating sling
   #player1
    sling1=pygame.image.load('Images/sling1.png')
    sling1=pygame.transform.scale(sling1,(80,160))
    sling1_rect=sling1.get_rect(center=(350,p.size[1]-168))
    sling2=pygame.image.load('Images/sling2.png')
    sling2=pygame.transform.scale(sling2,(50,100))
    sling2_rect=sling2.get_rect(center=(334,p.size[1]-198))
   #player2
    sling3=pygame.image.load('Images/sling3.png')
    sling3=pygame.transform.scale(sling3,(80,160))
    sling3_rect=sling3.get_rect(center=(p.size[0]-350,p.size[1]-168))
    sling4=pygame.image.load('Images/sling4.png')
    sling4=pygame.transform.scale(sling4,(50,100))
    sling4_rect=sling4.get_rect(center=(p.size[0]-334,p.size[1]-198))
#rendring name and making name rects
    font30=pygame.font.Font(None,30)
    font50=pygame.font.Font(None,50)
    name_surface1=font50.render(p.player1,True, p.Black)
    name_surface2=font50.render(p.player2,True, p.Black)
    name_rect1=name_surface1.get_rect(center=(400,200))
    name_rect2=name_surface2.get_rect(center=(p.size[0]-400,200))
#pause button 
    pause_surface=pygame.image.load('Images/pause.png')
    pause_surface=pygame.transform.scale(pause_surface,(40,40))
    pause_rect=pause_surface.get_rect(center=(50,50))
    settings_surface=pygame.image.load('Images/settings.png')
    settings_surface=pygame.transform.scale(settings_surface,(41,41))
    settings_rect=settings_surface.get_rect(center=(100,50))
    motiondots_text=font30.render('Turn motion dots off',True,p.White)
    motiontext_rect=motiondots_text.get_rect(center=(100,100))
#settings stats
#some variables
    dt=0
    mouse=False
    released=False
    extra=False
    abilityused=False
    generatebird=True
    falling1=False
    falling2=False
    player=random.randint(1,2)
    splayer=player
    #player=2
    x1=0
    y1=0
    x2=0
    y2=0
    c1=9
    disp1=0
    c2=-9
    disp2=0
    Time=pygame.time.get_ticks()
    end=False
    countdown=4
    countingdown=True
    paused=False
    settings=False
    pausetime=0
    initial=0
    final=0
    TotalPaused=0
    bot=False
#generating fortress
    block_surfacelist1,block_rectlist1,block_list1=generateFortress(1)
    block_surfacelist2,block_rectlist2,block_list2=generateFortress(2)
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if pause_rect.collidepoint(event.pos):
                    if paused:
                        paused=False
                        settings=False
                        final=pygame.time.get_ticks()
                        TotalPaused+=final-initial
                        pause_surface=pygame.image.load('Images/pause.png')
                        pause_surface=pygame.transform.scale(pause_surface,(width*0.03125,height*0.05556))
                    else:
                        paused=True
                        initial=pygame.time.get_ticks()
                        pause_surface=pygame.image.load('Images/resume.png')
                        pause_surface=pygame.transform.scale(pause_surface,(width*0.03125,height*0.05556))
                    continue
                if paused:
                    if settings_rect.collidepoint(event.pos):
                        if settings:
                            settings=False
                        else:
                            settings=True
                    elif motiontext_rect.collidepoint(event.pos):
                        if p.motiondots:
                            p.motiondots=False
                        else:
                            p.motiondots=True
            if not countingdown and not paused and not(bot and player==2):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mouse_x,mouse_y=event.pos
                    if not released:
                        mouse=True
                    if released and not (bot and player==2):
                        extra=True
                elif event.type==pygame.MOUSEMOTION:
                    if mouse:
                        mouse_x,mouse_y=event.pos
                elif event.type==pygame.MOUSEBUTTONUP:
                    if mouse:
                        time=pygame.time.get_ticks()
                        released=True
                        mouse=False
#drawing background and buttons
        screen.blit(background, (0,0))
        screen.blit(pause_surface,pause_rect)
        screen.blit(logo,(p.size[0]/2-250,10))
#rendring score and making score rects
        score_surface1=font50.render(str(p.score1),True, p.Black)
        score_surface2=font50.render(str(p.score2),True, p.Black)
        score_rect1=score_surface1.get_rect(center=(400,240))
        score_rect2=score_surface2.get_rect(center=(width-400,240))
#showing name and score
        screen.blit(name_surface1,name_rect1)
        screen.blit(name_surface2,name_rect2)
        screen.blit(score_surface1,score_rect1)
        screen.blit(score_surface2,score_rect2)
#countdown and timer
        if (pygame.time.get_ticks()-pausetime-Time)/1000<4:
            if not paused:
                countdown_surface=font50.render(str(countdown-1-(pygame.time.get_ticks()-pausetime-Time)//1000),True,p.Black)
                if countdown-1-(pygame.time.get_ticks()-pausetime-Time)//1000==0:
                    countdown_surface=font50.render('Start',True,p.Black)
                    countingdown=False
                countdown_rect=countdown_surface.get_rect(center=(width/2,height*0.486))
            screen.blit(countdown_surface,countdown_rect)
        if p.mode==1:
            if (pygame.time.get_ticks()-pausetime-Time)/1000<p.timelimit+5 and (pygame.time.get_ticks()-pausetime-Time)/1000>4:
                if not paused:
                    countdown2_surface=font50.render(str(p.timelimit+4-(pygame.time.get_ticks()-pausetime-Time)//1000),True,p.Black)
                if p.timelimit+4-(pygame.time.get_ticks()-pausetime-Time)//1000==0:
                    if p.score1==p.score2:
                        storeResult(2)
                    elif p.score1>p.score2:
                        storeResult(0)
                    else:
                        storeResult(1)
                    end=True
                else:
                    screen.blit(countdown2_surface,((width/2-20),240))
                if not end and all(not block for block in block_list1) and generatebird==True:
                    block_surfacelist1,block_rectlist1,block_list1=generateFortress(1)
                if not end and all(not block for block in block_list2) and generatebird==True:
                    block_surfacelist2,block_rectlist2,block_list2=generateFortress(2)
#drawing catapult
        screen.blit(sling1,sling1_rect)
        screen.blit(sling3,sling3_rect)
#checking game end
        if p.mode==0:
            end=gameEnd(player,generatebird,splayer)
#ending game
        if end:
            return end
#generating bird
        if not end:
            if generatebird:
                player=3-player
                bird,bird_surface,bird_rects=generateBird(player)
                extra=False
                abilityused=False
                generatebird=False
#checking if block is destroyed and deleting it 
        if not falling1:
            falling1,x1,y1=blockDestroyed(block_list1,block_surfacelist1,block_rectlist1,falling1,x1,y1)
        if not falling2:
            falling2,x2,y2=blockDestroyed(block_list2,block_surfacelist2,block_rectlist2,falling2,x2,y2)
#implementing falling effect of blocks
        falling1=fallingBlocks(x1,y1,block_list1,block_rectlist1,falling1)
        falling2=fallingBlocks(x2,y2,block_list2,block_rectlist2,falling2)        
#drawing fortress
        for i, block_col in enumerate(block_list1):
            for j, block in enumerate(block_col):
                screen.blit(block_surfacelist1[i][j],block_rectlist1[i][j])
        for i, block_col in enumerate(block_list2):
            for j, block in enumerate(block_col):
                screen.blit(block_surfacelist2[i][j],block_rectlist2[i][j])
#moving fortress
        if p.moving and not paused:
            c1,disp1=moveFortress(block_rectlist1,c1,1,disp1)
            c2,disp2=moveFortress(block_rectlist2,c2,2,disp2)
#drawing bird
        for i, bird_rect in enumerate(bird_rects):
            screen.blit(bird_surface,bird_rect)
#complete catapult drawing
        screen.blit(sling2,sling2_rect)
        screen.blit(sling4,sling4_rect)
#when held
        if mouse:
            speed,dirtheta,dist_sling=getSpeed(player,bird[0],mouse_x,mouse_y)
            x_speed=speed*math.cos(dirtheta)
            y_inispeed=speed*math.sin(dirtheta)
            y_speed=y_inispeed
            if p.motiondots:
                dot_positions=projectileDots(x_speed*dt,y_speed*dt,p.g*dt*dt,mouse_x,mouse_y)
                for i, dotposition in enumerate(dot_positions):
                    pygame.draw.circle(screen,p.White,dotposition,5)
            bird_rects[0].center=(mouse_x,mouse_y)
            bird[0].x_speed=x_speed
            bird[0].y_speed=y_speed
            if player==1:
                pygame.draw.line(screen,p.Black,(width*0.256,height*0.6903),(mouse_x,mouse_y),3)
                pygame.draw.line(screen,p.Black,(width*0.2797,height*0.6903),(mouse_x,mouse_y),3)
            else:
                pygame.draw.line(screen,p.Black,(width-(width*0.256),height*0.6903),(mouse_x,mouse_y),3)
                pygame.draw.line(screen,p.Black,(width-(width*0.2797),height*0.6903),(mouse_x,mouse_y),3)
        if player==2 and bot and not released and not countingdown and not paused:
            x_pos=random.randint(p.sling2[0],p.size[0])
            y_pos=random.randint(500,p.groundlevel)
            speed,dirtheta,dist_sling=getSpeed(player,bird[0],x_pos,y_pos)
            x_speed=speed*math.cos(dirtheta)
            y_inispeed=speed*math.sin(dirtheta)
            y_speed=y_inispeed
            if p.motiondots:
                dot_positions=projectileDots(x_speed*dt,y_speed*dt,p.g*dt*dt,x_pos,y_pos)
                for i, dotposition in enumerate(dot_positions):
                    pygame.draw.circle(screen,p.White,dotposition,5)
            bird_rects[0].center=(x_pos,y_pos)
            bird[0].x_speed=x_speed
            bird[0].y_speed=y_speed
            pygame.draw.line(screen,p.Black,(width-(width*0.256),height*0.6903),(x_pos,y_pos),3)
            pygame.draw.line(screen,p.Black,(width-(width*0.2797),height*0.6903),(x_pos,y_pos),3)
            time=pygame.time.get_ticks()
            released=True
#when released
        if released and not paused:
            for i, bird_rect in enumerate(bird_rects):
                if (pygame.time.get_ticks()-time)/1000>3.5 or bird_rect.left>p.size[0] or bird_rect.right<0:
                    released=False
                    generatebird=True
                if bot and player==2 and not abilityused:
                    if bird_rect==p.size[0]/2:
                        extra=bool(random.randint(0,1))
                        if extra:
                            abilityused=True
                bird[i].y_speed+=p.g*dt
                if p.wind:
                    if player==1:
                        bird[i].x_speed-=p.d*dt
                    else:
                        bird[i].x_speed+=p.d*dt
                bird_rects[i]=bird_rect.move(bird[i].x_speed*dt,bird[i].y_speed*dt)
                if extra and not abilityused:
                    bird_surface=extraAbility(bird,bird_rects,bird_surface,player)
                    abilityused=True
                if bird_rect.bottom>p.groundlevel:
                    bird[i].y_speed=-bird[i].y_speed*p.e
                    bird_rects[i].bottom=p.groundlevel
                if player==1:
                    bird_surface=detectCollision(1,bird[i],bird_rects[i],block_rectlist1,block_surfacelist1,block_list1,bird_surface)
                else:
                    bird_surface=detectCollision(2,bird[i],bird_rects[i],block_rectlist2,block_surfacelist2,block_list2,bird_surface)
#paused menu
        if paused:
            final=pygame.time.get_ticks()
            pausetime=TotalPaused+final-initial
            screen.blit(settings_surface,settings_rect)
            if settings:
                if p.motiondots:
                    motiondots_text=font30.render('Turn aim assist off',True,p.White)
                else:
                    motiondots_text=font30.render('Turn aim assist on',True,p.White)
                motiontext_rect=motiondots_text.get_rect(center=(width*0.117,height*0.1389))
                pygame.draw.rect(screen,p.Darkgrey,(motiontext_rect.left-5,motiontext_rect.top-5,(motiontext_rect.right-motiontext_rect.left)+10,(motiontext_rect.bottom-motiontext_rect.top+10)),border_radius=10)
                screen.blit(motiondots_text,motiontext_rect)
        pygame.display.flip()
        clock.tick(60)
        dt=clock.tick(60)/1000
    pygame.quit