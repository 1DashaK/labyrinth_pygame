import pygame
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_borders)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


pygame.init()
size = width, height = 1000, 600
screen = pygame.display.set_mode(size)

# группа, содержащая все стены
all_borders = pygame.sprite.Group()

horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()

borders = pygame.sprite.Group()
sprite = pygame.sprite.Sprite(borders)
sprite.rect = pygame.Rect(0, 0, 500, 1)
sprite1 = pygame.sprite.Sprite(borders)
sprite1.rect = pygame.Rect(0, 0, 1, 500)
sprite2 = pygame.sprite.Sprite(borders)
sprite2.rect = pygame.Rect(0, 500, 500, 1)
sprite3 = pygame.sprite.Sprite(borders)
sprite3.rect = pygame.Rect(0, 500, 1, 500)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.display.flip()
