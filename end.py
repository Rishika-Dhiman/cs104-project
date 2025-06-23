import pygame
import parameters as p

pygame.init()

def end_screen():

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

    result_surface=font40.render('Result',True,p.Black)
    result_rect=result_surface.get_rect(center=(p.size[0]/2,200))

    message=''

    if p.result==2:
        message="It's a draw"
    elif p.result==0:
        if p.player1!='':
            message=f"{p.player1} wins!"
        else:
            message="Player1 wins"
    else:
        if p.player2!='':
            message=f"{p.player2} wins!"
        else:
            message="Player2 wins!"

    message_surface=font60.render(message,True,p.Black)
    message_rect=message_surface.get_rect(center=(p.size[0]/2,300))

    playernames=font40.render(f"{p.player1}-{p.player2}",True,p.Black)
    playernames_rect=playernames.get_rect(center=(p.size[0]/2,500))
    playerscores=font40.render(f"{p.score1}-{p.score2}",True,p.Black)
    playerscores_rect=playerscores.get_rect(center=(p.size[0]/2,540))

    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

        screen.blit(background, (0,0))
        screen.blit(logo,(p.size[0]/2-250,10))
        screen.blit(result_surface,result_rect)
        screen.blit(message_surface,message_rect)
        screen.blit(playernames,playernames_rect)
        screen.blit(playerscores,playerscores_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit