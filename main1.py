import time
import pygame
from random import randint
from pygame import *
import math
from math import sqrt, acos
from main2 import *

YELLOW = (220, 200, 0)

pygame.init()

clock = pygame.time.Clock()
screen = display.set_mode((1680, 1000), vsync=1) # pygame.FULLSCREEN
display.set_caption('Little Adventure')

# icon = pygame.image.load('')
# pygame.display.set_icon()

width = 1680
height = 1050

bg_img = pygame.image.load('./Assets/grass.png')
bg_img = pygame.transform.scale(bg_img,(width,height))

pygame.mixer.music.load('/Users/yarik/PycharmProjects/MetroidParody/Assets/1-09. Beneath the Mask -instrumental version-.mp3')
pygame.mixer.music.set_volume(0.1)
# pygame.mixer.music.play()

UPPER = False
LOWER = False
RIGHT = False
LEFT = False
STOP = False

character_size = (96,120)
stay = []
ass = []
walk_right = []
walk_left = []
player_animations = (stay, ass, walk_right, walk_left)
trees = []
NPC_anim = []
NPC_dialog = []
cummen_img = []
Menu = []
is_quest_activated = 0
enemy_left = []
enemy_right = []
enemy = (enemy_left, enemy_right)

for i in range (1, 8):
    image = pygame.image.load(f'./Assets/Cummen/C{i}.png').convert_alpha()
    cummen_img.append(image)

for i in range (1, 3):
    image = pygame.image.load(f'./Assets/Tree{i}.png').convert_alpha()
    image = pygame.transform.scale(image,(350,400))
    trees.append(image)

for i in range (1, 6):
    image = pygame.image.load(f'./Assets/Rabbit_hero/Stay/S{i}.png').convert_alpha()
    image = pygame.transform.scale(image, character_size)
    stay.append(image)
    image = pygame.image.load(f'./Assets/Rabbit_hero/Back/B{i}.png').convert_alpha()
    image = pygame.transform.scale(image, character_size)
    ass.append(image)

for i in range (1, 8):
    image = pygame.image.load(f'./Assets/Rabbit_hero/Right/R{i}.png').convert_alpha()
    image = pygame.transform.scale(image, character_size)
    walk_right.append(image)
    image = pygame.image.load(f'./Assets/Rabbit_hero/Left/L{i}.png').convert_alpha()
    image = pygame.transform.scale(image, character_size)
    walk_left.append(image)

for i in range (1, 6):
    image = pygame.image.load(f'./Assets/NPC/S{i}.png').convert_alpha()
    image = pygame.transform.scale(image, character_size)
    NPC_anim.append(image)

for i in range (1, 3):
    image = pygame.image.load(f'./Assets/NPC/Texts/Text{i}.png').convert_alpha()
    image = pygame.transform.scale(image, (280, 240))
    NPC_dialog.append(image)

for i in range (1, 3):
    image = pygame.image.load(f'./Assets/NPC/Texts/Menu{i}.png').convert_alpha()
    image = pygame.transform.scale(image, (320, 200))
    Menu.append(image)

for i in range (1, 3):
    image = pygame.image.load(f'./Assets/Enemy/Left/Sprite_Boar{i}.png').convert_alpha()
    image = pygame.transform.scale(image, (120, 96))
    enemy[0].append(image)
    image = pygame.image.load(f'./Assets/Enemy/Right/Sprite_Boar{i}.png').convert_alpha()
    image = pygame.transform.scale(image, (120, 96))
    enemy[1].append(image)

carrot = pygame.image.load(f'./Assets/Carrot.png').convert_alpha()
carrot = pygame.transform.scale(carrot, (60,120))
carrot = pygame.transform.rotate(carrot, 90)
carrotflipped = pygame.transform.flip(carrot, True, False)
carrotrect = carrot.get_rect()

i = 0
x = 0
y = 0

class Cummen(pygame.sprite.Sprite):
    def __init__(self, a, b, num):
        pygame.sprite.Sprite.__init__(self)
        self.image = cummen_img[num]
        self.rect = self.image.get_rect()
        self.rect.center = (a, b)

    def update(self, x, y):
        self.rect.x += x
        self.rect.y += y

class Tree(pygame.sprite.Sprite):
    def __init__(self, a, b, num):
        pygame.sprite.Sprite.__init__(self)
        self.image = trees[num]
        # self.image = Surface((350,400))
        self.rect = self.image.get_rect()
        self.rect.topleft = (a, b)

    def update(self, x, y):
        self.rect.x += x
        self.rect.y += y

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = player_animations
        self.index = 0
        self.player_animation_i = 0
        self.image = self.images[self.index][self.player_animation_i]
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)

        self.current_time = 0

    def update (self, vector):
        if self.current_time < 60:
            self.current_time += 1
        else:
            self.current_time = 0

        self.index = vector
        if self.current_time % 5 == 0:
            if self.player_animation_i >= len(player_animations[self.index]):
                self.player_animation_i = 0
            else:
                self.image = player_animations[self.index][self.player_animation_i]
                self.player_animation_i += 1
            self.rect = self.image.get_rect()
            self.rect.center = (width / 2, height / 2)

class NPC(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = NPC_anim
        self.index = 0
        self.player_animation_i = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (width - 200, height/2)
        self.current_time = 0

    def update(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def animation(self):
        if self.current_time < 60:
            self.current_time += 1
        else:
            self.current_time = 0

        if self.current_time % 5 == 0:
            if self.index >= len(NPC_anim):
                self.index = 0
                self.image = NPC_anim[self.index]
            else:
                self.image = NPC_anim[self.index]
                self.index += 1

    def dialog(self):
        screen.blit(NPC_dialog[0], (self.rect.x - 200, self.rect.y - 250))
        objects.add(enemy1)
        pygame.display.update()
        # time.wait(1000)



class Enemy(pygame.sprite.Sprite):
    def __init__(self, a, b):
        pygame.sprite.Sprite.__init__(self)
        self.images = enemy
        self.index = 1
        self.enem_anim = 1
        self.image = self.images[self.index][self.enem_anim]
        self.rect = self.image.get_rect()
        self.rect.center = (a, b)
        self.current_time = 0

    def update(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def animation(self):
        if self.current_time < 60:
            self.current_time += 1
        else:
            self.current_time = 0

        # self.index = vector
        if self.current_time % 5 == 0:
            if self.enem_anim >= len(enemy[self.index]):
                self.enem_anim = 0
            else:
                self.image = enemy[self.index][self.enem_anim]
                self.enem_anim += 1
            # self.rect = self.image.get_rect()
            # self.rect.center = (width / 2, height / 2)

#player_animations[0][0]

def check_collisions(rect1, x, y, is_quest_activated):
    for obj in objects:
        if rect1.colliderect(obj.rect):

            print(obj.rect.topleft)
            print(obj.rect.center)
            print('================')
            print(rect1.center)

            if npc.rect == obj.rect:
                npc.dialog()
                is_quest_activated = 1

            angle = degree_beetwen_vectors((rect1.center[0], rect1.center[1]), (rect1.center[0] + 10, rect1.center[1]), (obj.rect.center[0], obj.rect.center[1]))

            if 0 < angle <= 22.5 or 337.5 < angle <= 0:
                x = x + 10
                objects.update(10, 0)
                print('a')
            elif 22.5 < angle <= 67.5:
                x = x + 10
                y = y + 10
                objects.update(10, 10)
            elif 67.5 < angle <= 112.5:
                y = y + 100
                objects.update(0, 10)
            elif 112.5 < angle <= 157.5:
                y = y + 10
                x = x - 10
                objects.update(-10, 10)
            elif 157.5 < angle <= 202.5:
                x = x - 10
                objects.update(-10, 0)
            elif 202.5 < angle <= 247.5:
                y = y - 10
                x = x - 10
                objects.update(-10, -10)
            elif 247.5 < angle <= 292.5:
                y = y - 10
                objects.update(0, -10)
            else:
                y = y + 10
                x = x + 10
                objects.update(10, 10)

    return x, y, is_quest_activated

def damage_to_enemies():
    pass

objects = pygame.sprite.Group()

# for j in range (0, 1):
#     for i in range (0, 1):
#         objects.add(Cummen(randint(0,width), randint(0,height),i))

objects.add(Tree(randint(0,width), randint(0,height),i))

npc = NPC()
objects.add(npc)

enemy1 =  Enemy(100,100)#(randint(-width, width * 2), randint(-height, height *2))
enemy2 =  Enemy(100,300)

cummen_rects = []
# cummen_rects.append(pygame.Rect())
vector = 0
rabbit = Player()




spawn = 0
run = True
motion = STOP
while run:

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

    screen.blit(rabbit.image, rabbit.rect)

    objects.draw(screen)
    npc.animation()
    enemy1.animation()

    # screen.blit(cumen_img, (randint(10, width + 10) + x, randint(10, height + 10) + y))

    if x == width:
        x = 0
    elif x ==-width:
        x = 0
    if y == height:
        y = 0
    elif y ==-height:
        y = 0

# Получение ивента нажатия на кнопку ходьбы
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

    if LOWER is False and UPPER is False and RIGHT is False and LEFT is False:
        vector = 0
    elif UPPER is True and RIGHT is True:
        vector = 2
        x -= 10
        y += 10
        objects.update(-10, +10)
    elif UPPER is True and LEFT is True:
        vector = 3
        x += 10
        y += 10
        objects.update(+10, +10)
    elif LOWER is True and RIGHT is True:
        vector = 2
        x -= 10
        y -= 10
        objects.update(-10, -10)
    elif LOWER is True and LEFT is True:
        vector = 3
        x += 10
        y -= 10
        objects.update(+10, -10)
    elif UPPER is True:
        vector = 1
        y += 10
        objects.update(0, +10)
    elif LEFT is True:
        vector = 3
        x += 10
        objects.update(+10, 0)
    elif RIGHT is True:
        vector = 2
        x -= 10
        objects.update(-10, 0)
    elif LOWER is True:
        vector = 0
        y -= 10
        objects.update(0, - 10)

    rabbit.update(vector)
    x, y, is_quest_activated = check_collisions(rabbit.rect, x, y, is_quest_activated)
    # print(rabbit.rect.x, rabbit.rect.y)


    if is_quest_activated == 1:
        screen.blit(Menu[0], (0,0))
        if vector == 2:
            screen.blit(carrot, (width/2 + 30, height/2 - 10))
        else:
            screen.blit(carrotflipped, (width / 2 - 155, height / 2 - 8))



    clock.tick(60)
    pygame.display.flip()
pygame.quit()