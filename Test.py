import pygame
import sys

GREEN = (200, 255, 200)
sc = pygame.display.set_mode((400, 400))
sc.fill(GREEN)

rect1 = pygame.Rect((0, 0, 30, 30))
rect2 = pygame.Rect((30, 30, 30, 30))

image = pygame.image.load(f'./Assets/NPC/S1.png').convert_alpha()
image = pygame.transform.scale(image, (96,120))
rect_of_image = image.get_rect()


# print(rect1.bottomright)  # (30, 30)
# print(rect2.bottomright)  # (60, 60)

rect_of_image.move_ip(10, 10)
# print(rect2.topleft)  # (40, 40)
#
# rect1.union_ip(rect2)
# print(rect1.width)  # 70

sc.blit(image, (0,0))
rect_of_image = image.get_rect()
print(rect_of_image.center)

pygame.display.update()

while 1:


    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()