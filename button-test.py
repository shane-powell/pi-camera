x = 0
y = 0
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

import pygame

from time import sleep


pygame.init()
pygame.font.init()
print(pygame.font.get_fonts())

screen = pygame.display.set_mode((520, 480), pygame.NOFRAME)
font = pygame.font.SysFont('freemono', 40)
gray = pygame.Color('gray15')
txt_placeholder = font.render('Buttons go here!', True, pygame.Color('seagreen1'))

while True:
    screen.fill(gray)
    screen.blit(txt_placeholder, (10, 10))
    # screen.blit(pygame.transform.rotate(screen, 270), (0, 0))
    pygame.display.flip()

