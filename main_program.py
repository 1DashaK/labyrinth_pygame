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

logo = load_image('Labyrinth.png')

game_over = pygame.sprite.Group()  # создание окончания игры

g_o_image = load_image('game_over.png')
game = pygame.sprite.Sprite(game_over)
game.image = g_o_image
game.rect = game.image.get_rect()
game.rect.top = 0
game.rect.left = 0

play = pygame.sprite.Group()  # создание кнопки начала

play_image = load_image('play.png')
play_image = pygame.transform.scale(play_image, (100, 100))
btn_play = pygame.sprite.Sprite(play)
btn_play.image = play_image
btn_play.rect = btn_play.image.get_rect()
btn_play.rect.top = 400
btn_play.rect.left = 200

restart = pygame.sprite.Group()  # создание кнопки заново

rest = pygame.sprite.Sprite(restart)
rest_image = load_image("restart.png")
rest_image = pygame.transform.scale(rest_image, (200, 100))
rest.image = rest_image
rest.rect = rest.image.get_rect()
rest.rect.left = 50
rest.rect.top = 270

all_sprites = pygame.sprite.Group()  # создание спрайта

sprite = pygame.sprite.Sprite(all_sprites)
ball_image = load_image("air_balloon.png")
ball_image = pygame.transform.scale(ball_image, (60, 60))
sprite.image = ball_image
sprite.rect = sprite.image.get_rect()
sprite.rect.left = 10
sprite.rect.top = 5

circle = pygame.sprite.Group()  # создание конца лабиринта

cir = pygame.sprite.Sprite(circle)
c_image = load_image("circle.png")
cir.image = c_image
cir.rect = sprite.image.get_rect()
cir.rect.left = 455
cir.rect.top = 560

win = pygame.sprite.Group()  # создание конца лабиринта

w = pygame.sprite.Sprite(win)
w_image = load_image("win.png")
w_image = pygame.transform.scale(w_image, (300, 400))
w.image = w_image
w.rect = sprite.image.get_rect()
w.rect.left = 100
w.rect.top = 100

clock = pygame.time.Clock()

is_game_over = False
is_first_level_end = False
is_start = False
is_win = False

motion = 'stop'

running = True
while running:
    if is_first_level_end:
        borders = borders_second_level
    else:
        borders = borders_first_level

    screen.fill((255, 255, 255))
    if (not is_game_over) and is_start and not is_win:
        borders.draw(screen)
        all_sprites.draw(screen)

        circle.draw(screen)

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

        if pygame.sprite.spritecollideany(sprite, circle):
            if is_first_level_end:
                is_win = True
                is_start = False
            else:
                is_first_level_end = True
                sprite.rect.left = 80
                sprite.rect.top = 80
                cir.rect.top = 535
                cir.rect.left = 80

        if motion == right:
            sprite.rect.x += 4
        elif motion == left:
            sprite.rect.x -= 4
        elif motion == up:
            sprite.rect.y -= 4
        elif motion == down:
            sprite.rect.y += 4

    elif is_game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_sprite = pygame.sprite.Sprite()
                mouse_sprite.rect = pygame.Rect(*pygame.mouse.get_pos(), 1, 1)
                collision = pygame.sprite.spritecollide(mouse_sprite, restart, False)
                if collision:
                    is_start = True
                    is_game_over = False
                    is_first_level_end = False
                    motion = stop
                    sprite.rect.left = 10
                    sprite.rect.top = 5
                    cir.rect.left = 455
                    cir.rect.top = 560

        game_over.draw(screen)
        restart.draw(screen)

    elif is_win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        win.draw(screen)

    elif not is_start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_sprite = pygame.sprite.Sprite()
                mouse_sprite.rect = pygame.Rect(*pygame.mouse.get_pos(), 1, 1)
                collision = pygame.sprite.spritecollide(mouse_sprite, play, False)
                if collision:
                    is_start = True

        play.draw(screen)
        screen.blit(logo, (100, 100))

    pygame.display.update()
    pygame.display.flip()
    clock.tick(15)
