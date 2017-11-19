'''
跑马灯，字符在滚动，可以查看支持的中文字体
'''
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

font = pygame.font.SysFont("方正兰亭超细黑简体", 40) #

#查看系统自带的字体
#print(pygame.font.get_fonts())

text_surface = font.render('好好学习', True, (0, 0, 255))

x = 0
y = (480 - text_surface.get_height()) #/2

backgroud = pygame.image.load('sushiplate.jpg')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(backgroud, (0, 0))

    x -= 1
    if x < -text_surface.get_width():
        x = 640 - text_surface.get_width()

    screen.blit(text_surface, (x, y))

    pygame.display.update()

