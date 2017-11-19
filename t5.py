'''
将字符存成图片，优秀
'''

my_name = "Will Kong"
import pygame
pygame.init()

my_font = pygame.font.SysFont('arial', 64)
name_surface = my_font.render(my_name, True, (1, 0, 0), (255, 255, 255))
pygame.image.save(name_surface, 'name.png')

