import pygame
import os
from maps.first_level import borders_first_level
from maps.second_level import borders_second_level


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


class Ball(pygame.sprite.Sprite):
    image = load_image("air_balloon.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Ball.image
        self.rect = self.image.get_rect()
        self.rect.x = 3
        self.rect.y = 3

    def update(self):
        pass


pygame.init()
size = width, height = 525, 675
screen = pygame.display.set_mode(size)

all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite(all_sprites)
ball_image = load_image("air_balloon.png")
ball_image = pygame.transform.scale(ball_image, (35, 35))
sprite.image = ball_image
sprite.rect = sprite.image.get_rect()
sprite.rect.left = 10
sprite.rect.top = 10
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    borders_first_level.draw(screen)
    all_sprites.draw(screen)
    pygame.display.flip()
