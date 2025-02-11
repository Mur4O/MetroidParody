import pygame

pygame.init()

W = 1680
H = 1050

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Класс Rect")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 60  # число кадров в секунду
clock = pygame.time.Clock()

character_size = (350,400)
picture = pygame.image.load(f'./Assets/Tree1.png').convert_alpha()
picture = pygame.transform.scale(picture, character_size)
rect = picture.get_rect()
print(rect)

surf = pygame.Surface((300,300))
surf.fill(BLUE)
rect1 = surf.get_rect()
# rect1.width = 350
# rect1.height = 400

print(rect1)

sc.fill(WHITE)
sc.blit(picture, (100, 50))
sc.blit(surf, (600, 50))
pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(FPS)