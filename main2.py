import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doodle Jump")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Настройки игры
FPS = 60
clock = pygame.time.Clock()
gravity = 0.5
player_speed = 8

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 100)
        self.velocity_y = 0
        self.on_platform = False

    def update(self, keys):
        # Движение по горизонтали
        if keys[pygame.K_LEFT]:
            self.rect.x -= player_speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += player_speed

        # Ограничение движения внутри экрана
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        # Гравитация
        self.velocity_y += gravity
        self.rect.y += self.velocity_y

        # Проверка на выход за верхний край экрана
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0

# Класс платформы
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = random.randint(50, 100)
        self.image = pygame.Surface((self.width, 10))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Движение платформ вниз
        self.rect.y += gravity * 2

        # Возвращение платформы наверх
        if self.rect.top > HEIGHT:
            self.rect.y = random.randint(-50, -10)
            self.rect.x = random.randint(0, WIDTH - self.width)

# Создание спрайтов
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# Создание начальных платформ
for i in range(8):
    plat = Platform(random.randint(0, WIDTH - 100), i * 100)
    all_sprites.add(plat)
    platforms.add(plat)

# Главный цикл игры
running = True
while running:
    clock.tick(FPS)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление спрайтов
    keys = pygame.key.get_pressed()
    player.update(keys)
    platforms.update()

    # Проверка столкновений с платформами
    if player.velocity_y > 0:
        hits = pygame.sprite.spritecollide(player, platforms, False)
        if hits:
            lowest = hits[0]
            for hit in hits:
                if hit.rect.bottom > lowest.rect.bottom:
                    lowest = hit
            if player.rect.bottom <= lowest.rect.top + 5 and not player.on_platform:
                player.velocity_y = -15
                player.on_platform = True
        else:
            player.on_platform = False

    # Отрисовка
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Обновление экрана
    pygame.display.flip()

pygame.quit()