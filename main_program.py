import pygame
import os
from maps.first_level import borders_first_level
from maps.second_level import borders_second_level

stop = 'stop'
right = 'right'
left = 'left'
up = 'up'
down = 'down'


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
size = width, height = 525, 675
screen = pygame.display.set_mode(size)

game_over = pygame.sprite.Group()  # создание окончания игры

image = load_image('game_over.png')
game = pygame.sprite.Sprite(game_over)
game.image = image
game.rect = game.image.get_rect()
game.rect.top = 0
game.rect.left = 0

all_sprites = pygame.sprite.Group()  # создание спрайта

sprite = pygame.sprite.Sprite(all_sprites)
ball_image = load_image("air_balloon.png")
ball_image = pygame.transform.scale(ball_image, (30, 30))
sprite.image = ball_image
sprite.rect = sprite.image.get_rect()
sprite.rect.left = 10
sprite.rect.top = 5

clock = pygame.time.Clock()

is_game_over = False

motion = 'stop'

running = True
while running:
    borders = borders_first_level

    screen.fill((255, 255, 255))

    if not is_game_over:
        borders_first_level.draw(screen)
        all_sprites.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    motion = left
                elif event.key == pygame.K_RIGHT:
                    motion = right
                elif event.key == pygame.K_UP:
                    motion = up
                elif event.key == pygame.K_DOWN:
                    motion = down
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP]:
                    motion = stop

        if pygame.sprite.spritecollideany(sprite, borders):
            game_over.draw(screen)
            is_game_over = True
        if motion == right:
            sprite.rect.x += 5
        elif motion == left:
            sprite.rect.x -= 5
        elif motion == up:
            sprite.rect.y -= 5
        elif motion == down:
            sprite.rect.y += 5

    if is_game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        game_over.draw(screen)

    pygame.display.update()
    pygame.display.flip()
    clock.tick(15)
