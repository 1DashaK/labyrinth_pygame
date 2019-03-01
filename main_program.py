import pygame
import os

stop = 'stop'
right = 'right'
left = 'left'
up = 'up'
down = 'down'
cell_size = 75


class Border(pygame.sprite.Sprite):  # класс стен
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(borders)
        self.image = pygame.Surface([abs(x2 - x1), abs(y2 - y1)])
        self.rect = pygame.Rect(x1, y1, abs(x2 - x1), abs(y2 - y1))
        if x1 == x2 - 2:  # вертикальная стена
            self.add(vertical_borders)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)


def load_image(name, colorkey=None):  # обработка изображения
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

borders = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()

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

circle = pygame.sprite.Group()  # создание перехода на следующий уровень лабиринта

cir = pygame.sprite.Sprite(circle)
c_image = load_image("circle.png")
cir.image = c_image
cir.rect = sprite.image.get_rect()

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
is_start = False
is_win = False

motion = 'stop'  # переменная, отвечающая за направление движения

levels = [f for f in os.listdir('maps')]  # скачивание уровней
levels.sort()
levels = levels[:-2]

last_level = 0  # выбор последнего уровня
f = open('maps/{}'.format(levels[last_level]))
rect = list(map(int, f.readline().strip().split()))  # установка спрайта в его начальную точку

sprite.rect.left = rect[0]
sprite.rect.top = rect[1]

rect = list(map(int, f.readline().strip().split()))  # установка перехода в его начальную точку

cir.rect.left = rect[0]
cir.rect.top = rect[1]

level = f.readlines()  # считывание из файла расположение стен
f.close()
for i in range(0, height, cell_size):  # создание стен
    for j in range(0, width, cell_size):
        if level[i // cell_size][j // cell_size] == '1':
            Border(j, i, j + 2, i + cell_size)
        if level[i // cell_size + 9][j // cell_size] == '1':
            Border(j, i, j + cell_size, i + 2)
running = True
while running:
    screen.fill((255, 255, 255))
    if (not is_game_over) and is_start and not is_win:  # цикл уровней
        vertical_borders.draw(screen)  # отрисовка стен
        horizontal_borders.draw(screen)  # отрисовка стен

        all_sprites.draw(screen)  # отрисовка спрайта

        circle.draw(screen)  # отрисовка перехода

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:  # движение по стрелкам
                if event.key == pygame.K_LEFT:
                    motion = left
                elif event.key == pygame.K_RIGHT:
                    motion = right
                elif event.key == pygame.K_UP:
                    motion = up
                elif event.key == pygame.K_DOWN:
                    motion = down

            elif event.type == pygame.KEYUP:  # остановка движения
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP]:
                    motion = stop

        if pygame.sprite.spritecollideany(sprite, borders):  # проверка на столкновение со стенами
            game_over.draw(screen)
            is_game_over = True

        if pygame.sprite.spritecollideany(sprite, circle):  # проверка на столкновение с переходом
            if last_level == len(levels) - 1:  # проверка, последний ли это уровень
                is_win = True
                is_start = False
            else:
                borders = pygame.sprite.Group()  # создание группы стен нового уровня
                horizontal_borders = pygame.sprite.Group()
                vertical_borders = pygame.sprite.Group()
                last_level += 1  #
                f = open('maps/{}'.format(levels[last_level]))

                rect = list(map(int, f.readline().strip().split()))  # установка спрайта в его начальную точку
                sprite.rect.left = rect[0]
                sprite.rect.top = rect[1]

                rect = list(map(int, f.readline().strip().split()))  # установка перехода в его начальную точку
                cir.rect.left = rect[0]
                cir.rect.top = rect[1]

                level = f.readlines()  # считывание из файла расположение стен
                f.close()
                for i in range(0, height, cell_size):  # создание стен
                    for j in range(0, width, cell_size):
                        if level[i // cell_size][j // cell_size] == '1':
                            Border(j, i, j + 2, i + cell_size)
                        if level[i // cell_size + 9][j // cell_size] == '1':
                            Border(j, i, j + cell_size, i + 2)

        if motion == right:  # движение спрайта
            sprite.rect.x += 4
        elif motion == left:
            sprite.rect.x -= 4
        elif motion == up:
            sprite.rect.y -= 4
        elif motion == down:
            sprite.rect.y += 4

    elif is_game_over:  # отрисовка проигрыша
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
                    last_level = 0
                    motion = stop
                    f = open('maps/{}'.format(levels[last_level]))

                    rect = list(map(int, f.readline().strip().split()))  # установка спрайта в его начальную точку
                    sprite.rect.left = rect[0]
                    sprite.rect.top = rect[1]

                    rect = list(map(int, f.readline().strip().split()))  # установка перехода в его начальную точку
                    cir.rect.left = rect[0]
                    cir.rect.top = rect[1]

                    level = f.readlines()  # считывание из файла расположение стен
                    f.close()
                    for i in range(0, height, cell_size):  # создание стен
                        for j in range(0, width, cell_size):
                            if level[i // cell_size][j // cell_size] == '1':
                                Border(j, i, j + 2, i + cell_size)
                            if level[i // cell_size + 9][j // cell_size] == '1':
                                Border(j, i, j + cell_size, i + 2)

        game_over.draw(screen)
        restart.draw(screen)

    elif is_win:  # отрисовка победы
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        win.draw(screen)

    elif not is_start:  # отрисовка начальной страницы
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

    pygame.display.flip()
    clock.tick(15)
