import pygame
from pygame import *

pygame.init()

clock = pygame.time.Clock()
screen = display.set_mode((1680, 1050)) # pygame.FULLSCREEN
display.set_caption('Some shit metroid game')

# icon = pygame.image.load('')
# pygame.display.set_icon()

width = 1680
height = 1050

bg_img = pygame.image.load('./Assets/back.png')
bg_img = pygame.transform.scale(bg_img,(width,height))

character_size = (96,120)

stay = (
    pygame.image.load('./Assets/Заяц, ну погоди/Стоит1.png'),
    pygame.image.load('./Assets/Заяц, ну погоди/Стоит2.png'),
    pygame.image.load('./Assets/Заяц, ну погоди/Стоит3.png'),
    pygame.image.load('./Assets/Заяц, ну погоди/Стоит4.png'),
    pygame.image.load('./Assets/Заяц, ну погоди/Стоит5.png'),
)

walk_right = (
    pygame.image.load('./Assets/Заяц, ну погоди/Идёт1.png'),
    pygame.image.load('./Assets/Заяц, ну погоди/Идёт2.png'),
    pygame.image.load('./Assets/Заяц, ну погоди/Идёт3.png'),
    pygame.image.load('./Assets/Заяц, ну погоди/Идёт4.png'),
    pygame.image.load('./Assets/Заяц, ну погоди/Идёт5.png'),
    pygame.image.load('./Assets/Заяц, ну погоди/Идёт6.png'),
    pygame.image.load('./Assets/Заяц, ну погоди/Идёт7.png'),
    pygame.image.load('./Assets/Заяц, ну погоди/Идёт8.png'),
)

walk_left = (
    pygame.image.load('./Assets/Заяц, ну погоди/Шагает1.png'),
    pygame.image.load('./Assets/Заяц, ну погоди/Шагает2.png'),
    pygame.image.load('./Assets/Заяц, ну погоди/Шагает3.png'),
    pygame.image.load('./Assets/Заяц, ну погоди/Шагает4.png'),
    pygame.image.load('./Assets/Заяц, ну погоди/Шагает5.png'),
    pygame.image.load('./Assets/Заяц, ну погоди/Шагает6.png'),
    pygame.image.load('./Assets/Заяц, ну погоди/Шагает7.png'),
    pygame.image.load('./Assets/Заяц, ну погоди/Шагает8.png'),
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