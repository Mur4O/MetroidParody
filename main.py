import time
import pygame
from random import randint
from pygame import *
import math
from math import sqrt, acos

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
pygame.mixer.music.play()

character_size = (96,120)

UPPER = False
LOWER = False
RIGHT = False
LEFT = False
STOP = False

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
    image = pygame.transform.scale(image, (280, 200))
    Menu.append(image)

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
        self.rect.center = (a, b)

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
            if self.player_animation_i >= len(player_animations[self.index]) - 1:
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

        if self.current_time < 60:
            self.current_time += 1
        else:
            self.current_time = 0

        if self.current_time % 5 == 0:
            if self.index >= len(NPC_anim) - 1:
                self.index = 0
            else:
                self.image = NPC_anim[self.index]
                self.index += 1

    def dialog(self):
        screen.blit(NPC_dialog[0], (self.rect.x - 200, self.rect.y - 250))
        pygame.display.update()
        time.wait(3000)


#player_animations[0][0]

def check_collizions(rect1, x, y, is_quest_activated):
    for obj in objects:
        if rect1.colliderect(obj.rect):
            if npc.rect == obj.rect:
                npc.dialog()
                is_quest_activated = 1
            point1 = (rect1.x, rect1.y)
            point2 = (rect1.x + rect1.width, rect1.y)
            point3 = (obj.rect.x, obj.rect.y)

            p1_p2_vector = (point1[0] - point2[0], point1[1] - point2[1])
            p1_p3_vector = (point1[0] - point3[0], point1[1] - point3[1])

            scalar = p1_p2_vector[0] * p1_p3_vector[0] + p1_p2_vector[1] * p1_p3_vector[1]
            mod_p1_p2 = sqrt(p1_p2_vector[0] ** 2 + p1_p2_vector[1] ** 2)
            mod_p1_p3 = sqrt(p1_p3_vector[0] ** 2 + p1_p3_vector[1] ** 2)

            if mod_p1_p2 * mod_p1_p3 == 0:
                arccos = 0.62
            else:
                cos = scalar / (mod_p1_p2 * mod_p1_p3)
                arccos = math.acos(cos)

            if point3[1] < point1[1]:
                arccos = -arccos

            if -0.52 <= arccos <= 0.52:
                x = x + 10
                objects.update(10, 0)
            elif 0.52 < arccos <= 1.05:
                x = x + 10
                y = y + 10
                objects.update(10, 10)
            elif 1.05 < arccos <= 2.09:
                y = y + 10
                objects.update(0, 10)
            elif 2.09 < arccos < 2.62:
                y = y + 10
                x = x - 10
                objects.update(-10, 10)
            elif arccos >= 2.62 or arccos <= -2.62:
                x = x - 10
                objects.update(-10, 0)
            elif -2.62 < arccos < -2.09:
                y = y - 10
                x = x - 10
                objects.update(-10, -10)
            elif -2.09 <= arccos < -1.05:
                y = y - 10
                objects.update(0, -10)
            elif -1.05 <= arccos < -0.52:
                y = y - 10
                x = x + 10
                objects.update(10, -10)
    return x, y, is_quest_activated






objects = pygame.sprite.Group()

for j in range (0, 2):
    for i in range (0, 7):
        objects.add(Cummen(randint(-width, width * 2), randint(-height, height *2),i))
for i in range (0, 7):    
    for i in range (0, 2):
        objects.add(Tree(randint(-width, width * 2), randint(-height, height *2),i))

npc = NPC()
objects.add(npc)




cummen_rects = []
# cummen_rects.append(pygame.Rect())
vector = 0
rabbit = Player()



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
    x, y, is_quest_activated = check_collizions(rabbit.rect, x, y, is_quest_activated)
    # print(rabbit.rect.x, rabbit.rect.y)

    if is_quest_activated == 1:
        # print('quest activated')
        screen.blit(Menu[0], (0,0))

    clock.tick(60)
    npc.update(0, 0)
    pygame.display.update()
pygame.quit()