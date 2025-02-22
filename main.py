import time
import pygame
from random import randint
from pygame import *
import math
from math import sqrt, acos
from main2 import *

YELLOW = (220, 200, 0)
BLACK = (0, 0, 0)

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
carrots = []
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
carrots.append(carrot)
carrots.append(carrotflipped)
# carrotrect = carrot.get_rect()

Fin = pygame.image.load(f'./Assets/NPC/Texts/Fin.png').convert_alpha()
Fin = pygame.transform.scale(Fin, (320, 200))

Ded = pygame.image.load(f'./Assets/NPC/Texts/YouKilled.png').convert_alpha()
Ded = pygame.transform.scale(Ded, (320, 200))


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
        pygame.display.flip()
        time.wait(1000)

    def dialog1(self):
        screen.blit(NPC_dialog[1], (self.rect.x - 200, self.rect.y - 250))
        pygame.display.flip()
        time.wait(1000)

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

    def walk(self, rect1):
        angle = degree_beetwen_vectors(self.rect.center, (self.rect.center[0] + 10, self.rect.center[1]), rect1.center)
        walk_x, walk_y = find_coordinates((0,0), 10, angle)
        self.update(walk_x, walk_y)

    def animation(self):
        if self.current_time < 60:
            self.current_time += 1
        else:
            self.current_time = 0

        if self.current_time % 5 == 0:
            if self.enem_anim >= len(enemy[self.index]):
                self.enem_anim = 0
            else:
                self.image = enemy[self.index][self.enem_anim]
                self.enem_anim += 1
            # self.rect = self.image.get_rect()
        # print(self.rect.center)
            # self.rect.center = (width / 2, height / 2)

class Carrot(pygame.sprite.Sprite):
    def __init__(self, a, b):
        pygame.sprite.Sprite.__init__(self)
        self.images = carrots
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (a, b)

    def update(self, x, y, ind):
        self.rect.x = x
        self.rect.y = y
        self.index = ind
        self.image = self.images[self.index]

weapons = pygame.sprite.Group()
weapon = Carrot(width/2 + 30, height/2 - 10)
weapons.add(weapon)

#player_animations[0][0]

def check_collisions(rect1, x, y, is_quest_activated, run):
    for obj in objects:
        if rect1.colliderect(obj.rect):
            if npc.rect == obj.rect and is_quest_activated == 0:
                npc.dialog()
                is_quest_activated = 1

            if npc.rect == obj.rect and is_quest_activated == 3:
                npc.dialog1()
                screen.fill(color=BLACK)
                screen.blit(Fin, (width / 2 - 100, height / 2 - 100))
                pygame.display.flip()
                time.wait(3000)
                run = False

            angle = degree_beetwen_vectors((rect1.center[0], rect1.center[1]), (rect1.center[0] + 10, rect1.center[1]), (obj.rect.center[0], obj.rect.center[1]))

            if 0 <= angle <= 45 or 315 <= angle < 360:
                x = x + 10
                objects.update(10, 0)
            elif 45 < angle < 135:
                y = y + 10
                objects.update(0, 10)
            elif 135 <= angle <= 225:
                x = x - 10
                objects.update(-10, 0)
            elif 225 < angle < 315:
                y = y - 10
                objects.update(0, -10)
    return x, y, is_quest_activated, run

def damage_to_enemies(carrot_rect, enemies, rabbit_rect, run):
    for enem in enemies:
        if carrot_rect.colliderect(enem.rect):
            enemies.remove(enem)
            objects.remove(enem)
            print(carrot_rect.center)

        if rabbit_rect.colliderect(enem.rect):
            screen.fill(color=BLACK)
            screen.blit(Ded, (width/2 - 100, height/2 - 100))
            pygame.display.flip()
            time.wait(3000)
            run = False

    return run





objects = pygame.sprite.Group()
enemies = pygame.sprite.Group()

for j in range (0, 2):
    for i in range (0, 7):
        objects.add(Cummen(randint(-width, width * 2), randint(-height, height *2),i))
for i in range (0, 7):    
    for i in range (0, 2):
        objects.add(Tree(randint(-width, width * 2), randint(-height, height *2),i))

npc = NPC()
objects.add(npc)

enemy1 =  Enemy(100,100)#(randint(-width, width * 2), randint(-height, height *2))
enemy2 =  Enemy(100,300)#(randint(-width, width * 2), randint(-height, height *2))

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

    for enem in enemies:
        enem.animation()

    objects.draw(screen)
    npc.animation()

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
        for enem in enemies:
            enem.walk(rabbit.rect)
        objects.update(-10, +10)
    elif UPPER is True and LEFT is True:
        vector = 3
        x += 10
        y += 10
        for enem in enemies:
            enem.walk(rabbit.rect)
        objects.update(+10, +10)
    elif LOWER is True and RIGHT is True:
        vector = 2
        x -= 10
        y -= 10
        for enem in enemies:
            enem.walk(rabbit.rect)
        objects.update(-10, -10)
    elif LOWER is True and LEFT is True:
        vector = 3
        x += 10
        y -= 10
        for enem in enemies:
            enem.walk(rabbit.rect)
        objects.update(+10, -10)
    elif UPPER is True:
        vector = 1
        y += 10
        for enem in enemies:
            enem.walk(rabbit.rect)
        objects.update(0, +10)
    elif LEFT is True:
        vector = 3
        x += 10
        for enem in enemies:
            enem.walk(rabbit.rect)
        objects.update(+10, 0)
    elif RIGHT is True:
        vector = 2
        x -= 10
        for enem in enemies:
            enem.walk(rabbit.rect)
        objects.update(-10, 0)
    elif LOWER is True:
        vector = 0
        y -= 10
        for enem in enemies:
            enem.walk(rabbit.rect)
        objects.update(0, - 10)

    rabbit.update(vector)


    if is_quest_activated == 1:
        screen.blit(Menu[0], (0,0))
        objects.add(enemy1)
        objects.add(enemy2)
        enemies.add(enemy1)
        enemies.add(enemy2)
        is_quest_activated = 2

    if is_quest_activated == 2:
        screen.blit(Menu[0], (0, 0))
        weapons.draw(screen)

        if vector == 2:
            weapon.update(width/2 + 30, height/2 - 10, 0)
            # screen.blit(carrot, (width/2 + 30, height/2 - 10))
            # carr_rect = carrot.get_rect()
        else:
            weapon.update(width / 2 - 155, height / 2 - 8, 1)
        #     carr_rect = carrotflipped.get_rect()

        run = damage_to_enemies(weapon.rect, enemies, rabbit.rect, run)

        if len(enemies) == 0:
            is_quest_activated = 3

    if is_quest_activated == 3:
        screen.blit(Menu[1], (0, 0))

    x, y, is_quest_activated, run = check_collisions(rabbit.rect, x, y, is_quest_activated, run)

    clock.tick(60)
    pygame.display.flip()
pygame.quit()