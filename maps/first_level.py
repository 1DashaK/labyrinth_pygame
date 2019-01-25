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


pygame.init()
size = width, height = 1000, 600
screen = pygame.display.set_mode(size)

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
