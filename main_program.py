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

all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite(all_sprites)
ball_image = load_image("ball.png")
ball_image = pygame.transform.scale(ball_image, (50, 50))
sprite.image = ball_image
sprite.rect = sprite.image.get_rect()
sprite.rect.left = 10
sprite.rect.top = 10
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
