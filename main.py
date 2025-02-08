import pygame
from random import randint
from pygame import *


pygame.init()

clock = pygame.time.Clock()
screen = display.set_mode((1680, 1000)) # pygame.FULLSCREEN
display.set_caption('Metroid game')

# icon = pygame.image.load('')
# pygame.display.set_icon()

width = 1680
height = 1050

bg_img = pygame.image.load('./Assets/grass.png')
bg_img = pygame.transform.scale(bg_img,(width,height))

character_size = (96,120)

UPPER = False
LOWER = False
RIGHT = False
LEFT = False
STOP = False

stay = (
    pygame.image.load('./Assets/Rabbit_hero/Stay/S1.png'),
    pygame.image.load('./Assets/Rabbit_hero/Stay/S2.png'),
    pygame.image.load('./Assets/Rabbit_hero/Stay/S3.png'),
    pygame.image.load('./Assets/Rabbit_hero/Stay/S4.png'),
    pygame.image.load('./Assets/Rabbit_hero/Stay/S5.png')
)

walk_right = (
    pygame.image.load('Assets/Rabbit_hero/Right/R1.png'),
    pygame.image.load('Assets/Rabbit_hero/Right/R2.png'),
    pygame.image.load('Assets/Rabbit_hero/Right/R3.png'),
    pygame.image.load('Assets/Rabbit_hero/Right/R4.png'),
    pygame.image.load('Assets/Rabbit_hero/Right/R5.png'),
    pygame.image.load('Assets/Rabbit_hero/Right/R6.png'),
    pygame.image.load('Assets/Rabbit_hero/Right/R7.png'),
    pygame.image.load('Assets/Rabbit_hero/Right/R8.png')
)

walk_left = (
    pygame.image.load('Assets/Rabbit_hero/Left/L1.png'),
    pygame.image.load('Assets/Rabbit_hero/Left/L2.png'),
    pygame.image.load('Assets/Rabbit_hero/Left/L3.png'),
    pygame.image.load('Assets/Rabbit_hero/Left/L4.png'),
    pygame.image.load('Assets/Rabbit_hero/Left/L5.png'),
    pygame.image.load('Assets/Rabbit_hero/Left/L6.png'),
    pygame.image.load('Assets/Rabbit_hero/Left/L7.png'),
    pygame.image.load('Assets/Rabbit_hero/Left/L8.png')
)

ass = (
    pygame.image.load('./Assets/Rabbit_hero/Back/B1.png'),
    pygame.image.load('./Assets/Rabbit_hero/Back/B2.png'),
    pygame.image.load('./Assets/Rabbit_hero/Back/B3.png'),
    pygame.image.load('./Assets/Rabbit_hero/Back/B4.png'),
    pygame.image.load('./Assets/Rabbit_hero/Back/B5.png')
)

cummen = (
    pygame.image.load('./Assets/Cummen/C1.png'),
    pygame.image.load('./Assets/Cummen/C2.png'),
    pygame.image.load('./Assets/Cummen/C3.png'),
    pygame.image.load('./Assets/Cummen/C4.png'),
    pygame.image.load('./Assets/Cummen/C5.png'),
    pygame.image.load('./Assets/Cummen/C6.png'),
    pygame.image.load('./Assets/Cummen/C7.png'),
)



cummens = pygame.sprite.Group()
i = 0
player_animation_i = 0
x = 0
y = 0

class Cummen(pygame.sprite.Sprite):
    def __init__(self, a, b, path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(center=(a, b))

    def update(self, x, y):
        self.rect.x += x
        self.rect.y += y

cummen_counter = 0
cummen_sprite = 0

cummen1 = Cummen(width/2, height/2, f'/Users/yarik/PycharmProjects/MetroidParody/Assets/Cummen/C1.png')

cumen_img = pygame.image.load('./Assets/Cummen/C1.png')

cummen_rects = []
# cummen_rects.append(pygame.Rect())

run = True
motion = STOP
animation = stay[player_animation_i]
while run:



    # cummens.draw(screen)

    screen.fill((0,0,0))
    screen.blit(bg_img, (x, y))
    screen.blit(bg_img, (width + x, y))
    screen.blit(bg_img, (-width + x, y))
    screen.blit(bg_img, (x, height + y))
    screen.blit(bg_img, (x, -height + y))
    screen.blit(bg_img, (width + x, height + y))
    screen.blit(bg_img, (- width + x, height + y))
    screen.blit(bg_img, (width + x, - height + y))
    screen.blit(bg_img, (- width + x, - height + y))

    screen.blit(cumen_img, (width / 2 + x, height / 2 + y))



    if x == width:
        x = 0
    elif x ==-width:
        x = 0
    if y == height:
        y = 0
    elif y ==-height:
        y = 0

    for i in event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_a:
                LEFT = True
            if i.key == pygame.K_d:
                RIGHT = True
            if i.key == pygame.K_w:
                UPPER = True
            if i.key == pygame.K_s:
                LOWER = True
        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_a:
                LEFT = False
            if i.key == pygame.K_d:
                RIGHT = False
            if i.key == pygame.K_w:
                UPPER = False
            if i.key == pygame.K_s:
                LOWER = False

    old_motion = motion

    if old_motion != motion:
        player_animation_i = 0

    if LOWER is False and UPPER is False and RIGHT is False and LEFT is False:
        try:
            screen.blit(pygame.transform.scale(stay[player_animation_i], character_size), (width / 2, height / 2))
            clock.tick(10)
            if player_animation_i < len(stay) - 1:
                player_animation_i += 1
            else:
                player_animation_i = 0
        except:
            player_animation_i = 0
            screen.blit(pygame.transform.scale(stay[player_animation_i], character_size), (width / 2, height / 2))
    elif UPPER is True and RIGHT is True:
        x -= 10
        y += 10
        screen.blit(pygame.transform.scale(walk_right[player_animation_i], character_size), (width / 2, height / 2))
        if player_animation_i < len(walk_left) - 1:
            player_animation_i += 1
        else:
            player_animation_i = 0
    elif UPPER is True and LEFT is True:
        x += 10
        y += 10
        screen.blit(pygame.transform.scale(walk_left[player_animation_i], character_size), (width / 2, height / 2))
        if player_animation_i < len(walk_left) - 1:
            player_animation_i += 1
        else:
            player_animation_i = 0
    elif LOWER is True and RIGHT is True:
        x -= 10
        y -= 10
        screen.blit(pygame.transform.scale(walk_right[player_animation_i], character_size), (width / 2, height / 2))
        if player_animation_i < len(walk_left) - 1:
            player_animation_i += 1
        else:
            player_animation_i = 0
    elif LOWER is True and LEFT is True:
        x += 10
        y -= 10
        screen.blit(pygame.transform.scale(walk_left[player_animation_i], character_size), (width / 2, height / 2))
        if player_animation_i < len(walk_left) - 1:
            player_animation_i += 1
        else:
            player_animation_i = 0
    elif UPPER is True:
        y += 10
        try:
            screen.blit(pygame.transform.scale(ass[player_animation_i], character_size), (width / 2, height / 2))
            if player_animation_i < len(stay) - 1:
                player_animation_i += 1
            else:
                player_animation_i = 0
        except:
            player_animation_i = 0
            screen.blit(pygame.transform.scale(ass[player_animation_i], character_size), (width / 2, height / 2))
    elif LEFT is True:
        x += 10
        screen.blit(pygame.transform.scale(walk_left[player_animation_i], character_size), (width / 2, height / 2))
        if player_animation_i < len(walk_left) - 1:
            player_animation_i += 1
        else:
            player_animation_i = 0
    elif RIGHT is True:
        x -= 10
        screen.blit(pygame.transform.scale(walk_right[player_animation_i], character_size), (width / 2, height / 2))
        if player_animation_i < len(walk_left) - 1:
            player_animation_i += 1
        else:
            player_animation_i = 0
    elif LOWER is True:
        y -= 10
        try:
            screen.blit(pygame.transform.scale(stay[player_animation_i], character_size), (width / 2, height / 2))
            if player_animation_i < len(stay) - 1:
                player_animation_i += 1
            else:
                player_animation_i = 0
        except:
            player_animation_i = 0
            screen.blit(pygame.transform.scale(stay[player_animation_i], character_size), (width / 2, height / 2))

    clock.tick(60)
    pygame.display.update()
pygame.quit()