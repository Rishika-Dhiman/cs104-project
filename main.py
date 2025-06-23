import pygame
from interface import interface_screen
from game import gameStart
from end import end_screen

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('bgm.ogg')
pygame.mixer.music.play(-1)

start=False
end=False

start=interface_screen(start)

if(start):
    end=gameStart()

if(end):
    end_screen()