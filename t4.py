'''
键盘摁下f，可以全屏
'''
background_image_filename = 'sushiplate.jpg'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#输出显卡支持的显示分辨率
#print(pygame.display.list_modes())

screen = pygame.display.set_mode((640,480), 0, 32)
background = pygame.image.load(background_image_filename)

Fullscreen = False

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    if event.type == KEYDOWN:
        if event.key == K_f:
            Fullscreen = not Fullscreen
            if Fullscreen:
                screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)
            else:
                screen = pygame.display.set_mode((640, 480), 0, 32)

    screen.blit(background, (0, 0))
    pygame.display.update()