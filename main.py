import pygame
import os
from pygame import *

pygame.init()

clock = pygame.time.Clock()
screen = display.set_mode((1680, 1050)) # pygame.FULLSCREEN
display.set_caption('Some shit metroid game')

# icon = pygame.image.load('')
# pygame.display.set_icon()

width = 1680
height = 1050

bg_img = pygame.image.load('./Assets/back.png', )
bg_img = pygame.transform.scale(bg_img,(width,height))

character_size = (96,120)

stay = (
    pygame.image.load('Assets/Rabbit_hero/S1.png'),
    pygame.image.load('Assets/Rabbit_hero/S2.png'),
    pygame.image.load('Assets/Rabbit_hero/S3.png'),
    pygame.image.load('Assets/Rabbit_hero/S4.png'),
    pygame.image.load('Assets/Rabbit_hero/S5.png'),
)

walk_right = (
    pygame.image.load('Assets/Rabbit_hero/R1.png'),
    pygame.image.load('Assets/Rabbit_hero/R2.png'),
    pygame.image.load('Assets/Rabbit_hero/R3.png'),
    pygame.image.load('Assets/Rabbit_hero/R4.png'),
    pygame.image.load('Assets/Rabbit_hero/R5.png'),
    pygame.image.load('Assets/Rabbit_hero/R6.png'),
    pygame.image.load('Assets/Rabbit_hero/R7.png'),
    pygame.image.load('Assets/Rabbit_hero/R8.png'),
)

walk_left = (
    pygame.image.load('Assets/Rabbit_hero/L1.png'),
    pygame.image.load('Assets/Rabbit_hero/L2.png'),
    pygame.image.load('Assets/Rabbit_hero/L3.png'),
    pygame.image.load('Assets/Rabbit_hero/L4.png'),
    pygame.image.load('Assets/Rabbit_hero/L5.png'),
    pygame.image.load('Assets/Rabbit_hero/L6.png'),
    pygame.image.load('Assets/Rabbit_hero/L7.png'),
    pygame.image.load('Assets/Rabbit_hero/L8.png'),
)

i = 0
player_animation_i = 0
player_speed = 5
run = True
while run:

    screen.blit(bg_img,(0,0))
    screen.blit(pygame.transform.scale(stay[player_animation_i], character_size),(100,800))

    if player_animation_i == 4:
        player_animation_i = 0
    else:
        player_animation_i += 1




    for e in event.get():
        if e.type == pygame.QUIT:
            run = False

    clock.tick(10)

    pygame.display.update()

pygame.quit()