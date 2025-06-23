import pygame
import parameters as p
from parameters import storeName,setWind,setMoving,setMode,setGrid,setDifficulty

pygame.init()

def interface_screen(start):
    
    screen=pygame.display.set_mode(p.size)
    pygame.display.set_caption('Angry Birds')
    clock=pygame.time.Clock()

    background=pygame.image.load('Images/background.jpg')
    background=pygame.transform.scale(background, (p.size))
    logo=pygame.image.load('Images/Angry_Birds_logo.png')
    logo=pygame.transform.smoothscale(logo,(500,113.33))

    font40=pygame.font.Font(None, 40)
    font30=pygame.font.Font(None, 30)
    font60=pygame.font.Font(None, 60)

    text1=''
    text2=''
    name1=False
    name2=False
#input text
    text_surface1=font40.render(text1,True, p.White)
    text_surface2=font40.render(text2,True, p.White)

    text_rect1=pygame.Rect(200,180,100,40)
    text_rect2=pygame.Rect(200,300,100,40)

    prompt1='Enter Player1 name'
    prompt2='Enter Player2 name'

    prompt_surface1=font40.render(prompt1,True, p.Black)
    prompt_surface2=font40.render(prompt2,True, p.Black)
#mode surface and rect
    modeprompt_surface=font40.render('Select Mode',True,p.Black)
    modeprompt_rect=modeprompt_surface.get_rect(center=(270,400))
    mode1_surface=font30.render('Last Stand',True,p.White)
    mode1_rect=mode1_surface.get_rect(center=(270,460))
    mode2_surface=font30.render('Timed Assault',True,p.White)
    mode2_rect=mode2_surface.get_rect(center=(270,540))
#grid surfaces and rects
    gridprompt_surface=font40.render('Select fortress shape',True,p.Black)
    gridprompt_rect=gridprompt_surface.get_rect(center=(1000,380))
    width_surface=font30.render('Width',True,p.Black)
    width_rect=width_surface.get_rect(center=(900,460))
    height_surface=font30.render('Height',True,p.Black)
    height_rect=height_surface.get_rect(center=(900,540))
    widthnums=[]
    widthrects=[]
    heightnums=[]
    heightrects=[]
    for i in range(1,6):
        widthnums.append(font30.render(str(i),True,p.White))
        widthrects.append(widthnums[i-1].get_rect(center=(920+40*i,460)))
    for i in range(1,8):
        heightnums.append(font30.render(str(i),True,p.White))
        heightrects.append(heightnums[i-1].get_rect(center=(920+40*i,540)))
#when selected messages
    modeselect=font40.render('Mode selected',True,p.Black)
    #grid select is inside while loop
    heightselect=font30.render('Height selected',True,p.Black)
    widthselect=font30.render('Width selected',True,p.Black)
#playbutton
    playbutton=pygame.image.load('Images/playbutton.png')  
    playbutton=pygame.transform.scale(playbutton,(180,110))
    playbutton_rect=playbutton.get_rect(center=(p.size[0]/2,500))
#difficulty
    difficultyprompt=font40.render('Select Difficulty',True,p.Black)
    Beginner_surface=font30.render('Beginner mode',True,p.White)
    Intermediate_surface=font30.render('Intermediate mode',True,p.White)
    Advanced_surface=font30.render('Advanced mode',True,p.White)
    Beginner_rect=Beginner_surface.get_rect(center=(900+Beginner_surface.get_width()/2,220))
    Intermediate_rect=Intermediate_surface.get_rect(center=(900+Intermediate_surface.get_width()/2,280))
    Advanced_rect=Advanced_surface.get_rect(center=(900+Advanced_surface.get_width()/2,340))
    OR_surface=font40.render('OR',True,p.Black)
    custom_surface=font40.render('Select Custom Settings',True,p.White)
    custom_rect=custom_surface.get_rect(center=(850+custom_surface.get_width()/2,500))
#wind prompt
    wind_prompt=font40.render('Wind',True,p.Black)
    moving_prompt=font40.render('Moving blocks',True,p.Black)
    on_surface=font30.render('On',True,p.White)
    off_surface=font30.render('Off',True,p.White)
    on_rectw=on_surface.get_rect(center=(940,210))
    off_rectw=off_surface.get_rect(center=(1100,210))
    on_rectm=on_surface.get_rect(center=(940,325))
    off_rectm=off_surface.get_rect(center=(1100,325))
#some variables
    gridset=False
    width=False
    height=False
    modeset=False
    windset=False
    movingset=False
    difficultyset=False
    custom=False
    a=0
    b=0
    ready=False
    running=True

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=event.pos
                if(text_rect1.inflate(20,20).collidepoint(mouse_x,mouse_y)):
                    name1=True
                    name2=False
                elif(text_rect2.inflate(20,20).collidepoint(mouse_x,mouse_y)):
                    name2=True
                    name1=False
                elif(playbutton_rect.collidepoint(mouse_x,mouse_y)) and ready:
                    storeName(text1,text2)
                    start=True
                    return start
                elif mode1_rect.inflate(10,10).collidepoint(mouse_x,mouse_y):
                    setMode(0)
                    modeset=True
                elif mode2_rect.inflate(10,10).collidepoint(mouse_x,mouse_y):
                    setMode(1)
                    modeset=True
                elif not custom:
                    if Beginner_rect.collidepoint(mouse_x,mouse_y):
                        difficultyset=True
                        setDifficulty(1)
                        difficultyselected=font40.render('Difficulty Selected: Beginner',True,p.Black)
                    elif Intermediate_rect.collidepoint(mouse_x,mouse_y):
                        difficultyset=True
                        setDifficulty(2)
                        difficultyselected=font40.render('Difficulty Selected: Intermediate',True,p.Black)
                    elif Advanced_rect.collidepoint(mouse_x,mouse_y):
                        difficultyset=True
                        setDifficulty(3)
                        difficultyselected=font40.render('Difficulty Selected: Advanced',True,p.Black)
                    elif custom_rect.inflate(10,10).collidepoint(mouse_x,mouse_y):
                        custom=True
                        break
                elif custom:
                    if on_rectw.inflate(20,20).collidepoint(mouse_x,mouse_y):
                        windselect=font40.render('Wind mode is on',True,p.Black)
                        setWind(True)
                        windset=True
                    elif off_rectw.inflate(20,20).collidepoint(mouse_x,mouse_y):
                        windselect=font40.render('Wind mode is off',True,p.Black)
                        setWind(False)
                        windset=True
                    elif on_rectm.inflate(20,20).collidepoint(mouse_x,mouse_y):
                        movingselect=font40.render('Moving blocks is on',True,p.Black)
                        setMoving(True)
                        movingset=True
                    elif off_rectm.inflate(20,20).collidepoint(mouse_x,mouse_y):
                        movingselect=font40.render('Moving blocks is off',True,p.Black)
                        setMoving(False)
                        movingset=True
                    else:
                        for i, heightrect in enumerate(heightrects):
                            if heightrect.inflate(20,20).collidepoint(mouse_x,mouse_y):
                                b=i+1
                                height=True
                        for i, widthrect in enumerate(widthrects):
                            if widthrect.inflate(20,20).collidepoint(mouse_x,mouse_y):
                                a=i+1
                                width=True
                else:
                    name1=False
                    name2=False
            if(name1):
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_BACKSPACE:
                        text1=text1[:-1]
                    elif event.key == pygame.K_RETURN:
                        p.player1=text1
                        name1=False
                    else:
                        text1+=event.unicode
                text_surface1=font40.render(text1,True,p.White)
                text_rect1=text_surface1.get_rect(center=(200+text_surface1.get_width()/2,200))
            elif(name2):
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_BACKSPACE:
                        text2=text2[:-1]
                    elif event.key==pygame.K_RETURN:
                        p.player2=text2
                        name2=False
                    else:
                        text2+=event.unicode
                text_surface2=font40.render(text2,True,p.White)
                text_rect2=text_surface2.get_rect(center=(200+text_surface2.get_width()/2,320))
            
        #ready=text1 and text2 and modeset and (difficultyset or (windset and movingset and gridset))
        ready=True
        screen.blit(background,(0,0))
        screen.blit(logo,(p.size[0]/2-250,10))
        if ready:
            screen.blit(playbutton,playbutton_rect)
        pygame.draw.rect(screen,p.Darkgrey,(text_rect1.left-5,text_rect1.top-5,(text_rect1.right-text_rect1.left)+10,(text_rect1.bottom-text_rect1.top+10)),border_radius=10)
        pygame.draw.rect(screen,p.Darkgrey,(text_rect2.left-5,text_rect2.top-5,(text_rect2.right-text_rect2.left)+10,(text_rect2.bottom-text_rect2.top+10)),border_radius=10)
#bliting name prompt and input surface       
        screen.blit(prompt_surface1,(200,140))
        screen.blit(prompt_surface2,(200,260))
        screen.blit(text_surface1,text_rect1)
        screen.blit(text_surface2,text_rect2)
#Mode select
        if not modeset:
            screen.blit(modeprompt_surface,modeprompt_rect)
            pygame.draw.rect(screen,p.Darkgrey,(mode1_rect.left-5,mode1_rect.top-5,(mode1_rect.right-mode1_rect.left)+10,(mode1_rect.bottom-mode1_rect.top+10)),border_radius=10)
            pygame.draw.rect(screen,p.Darkgrey,(mode2_rect.left-5,mode2_rect.top-5,(mode2_rect.right-mode2_rect.left)+10,(mode2_rect.bottom-mode2_rect.top+10)),border_radius=10)
            screen.blit(mode1_surface,mode1_rect)
            screen.blit(mode2_surface,mode2_rect)
        else:
            screen.blit(modeselect,(200,380))
#difficulty
        if not custom:
            if not difficultyset:
                pygame.draw.rect(screen,p.Darkgrey,(Beginner_rect.left-5,Beginner_rect.top-5,(Beginner_rect.right-Beginner_rect.left)+10,(Beginner_rect.bottom-Beginner_rect.top+10)),border_radius=10)
                pygame.draw.rect(screen,p.Darkgrey,(Intermediate_rect.left-5,Intermediate_rect.top-5,(Intermediate_rect.right-Intermediate_rect.left)+10,(Intermediate_rect.bottom-Intermediate_rect.top+10)),border_radius=10)
                pygame.draw.rect(screen,p.Darkgrey,(Advanced_rect.left-5,Advanced_rect.top-5,(Advanced_rect.right-Advanced_rect.left)+10,(Advanced_rect.bottom-Advanced_rect.top+10)),border_radius=10)
                pygame.draw.rect(screen,p.Darkgrey,(custom_rect.left-5,custom_rect.top-5,(custom_rect.right-custom_rect.left)+10,(custom_rect.bottom-custom_rect.top+10)),border_radius=10)
                screen.blit(difficultyprompt,(850,140))
                screen.blit(Beginner_surface,Beginner_rect)
                screen.blit(Intermediate_surface,Intermediate_rect)
                screen.blit(Advanced_surface,Advanced_rect)
                screen.blit(OR_surface,(850,400))
                screen.blit(custom_surface,custom_rect)
        if difficultyset:
            screen.blit(difficultyselected,(830,200))
#custom options
        if custom:
    #Wind option
            if not windset:
                pygame.draw.rect(screen,p.Darkgrey,(on_rectw.left-5,on_rectw.top-5,(on_rectw.right-on_rectw.left)+10,(on_rectw.bottom-on_rectw.top+10)),border_radius=10)
                pygame.draw.rect(screen,p.Darkgrey,(off_rectw.left-5,off_rectw.top-5,(off_rectw.right-off_rectw.left)+10,(off_rectw.bottom-off_rectw.top+10)),border_radius=10)
                screen.blit(wind_prompt,(850,150))
                screen.blit(on_surface,on_rectw)
                screen.blit(off_surface,off_rectw)
            else:
                screen.blit(windselect,(850,150))
    #Moving option        
            if not movingset:
                pygame.draw.rect(screen,p.Darkgrey,(on_rectm.left-5,on_rectm.top-5,(on_rectm.right-on_rectm.left)+10,(on_rectm.bottom-on_rectm.top+10)),border_radius=10)
                pygame.draw.rect(screen,p.Darkgrey,(off_rectm.left-5,off_rectm.top-5,(off_rectm.right-off_rectm.left)+10,(off_rectm.bottom-off_rectm.top+10)),border_radius=10)
                screen.blit(moving_prompt,(850,250))
                screen.blit(on_surface,on_rectm)
                screen.blit(off_surface,off_rectm)
            else:
                screen.blit(movingselect,(850,250))
            if height and width:
            #updating grid select text
                gridselect=font40.render(f'Fortress dimension : {a}x{b}',True,p.Black)
                gridset=True
    #Grid select
            if not gridset:
                screen.blit(gridprompt_surface,(850,380))
                screen.blit(width_surface,width_rect)
                screen.blit(height_surface,height_rect)
                if not height:
                    for i in range(1,8):
                        pygame.draw.rect(screen,p.Darkgrey,(heightrects[i-1].left-5,heightrects[i-1].top-5,(heightrects[i-1].right-heightrects[i-1].left)+10,(heightrects[i-1].bottom-heightrects[i-1].top+10)),border_radius=10)
                        screen.blit(heightnums[i-1],heightrects[i-1])
                else:
                    screen.blit(heightselect,(1000,525))
                if not width:
                    for i in range(1,6):
                        pygame.draw.rect(screen,p.Darkgrey,(widthrects[i-1].left-5,widthrects[i-1].top-5,(widthrects[i-1].right-widthrects[i-1].left)+10,(widthrects[i-1].bottom-widthrects[i-1].top+10)),border_radius=10)
                        screen.blit(widthnums[i-1],widthrects[i-1])
                else:
                    screen.blit(widthselect,(1000,445))
            else:
                screen.blit(gridselect,(850,380))
                setGrid(a,b)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit
