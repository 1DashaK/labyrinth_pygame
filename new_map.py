import pygame

number = int(input())
width = 525
height = 675
cell_size = 75
vert_borders = [[0] * (width // cell_size) for i in range(0, height, cell_size)]
hor_borders = [[0] * (width // cell_size) for i in range(0, height, cell_size)]


class Border(pygame.sprite.Sprite):  # класс стен
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_borders)
        self.image = pygame.Surface([abs(x2 - x1), abs(y2 - y1)])
        self.rect = pygame.Rect(x1, y1, abs(x2 - x1), abs(y2 - y1))
        if x1 == x2 - 2:  # вертикальная стена
            self.add(vertical_borders)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)


all_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
for i in range(0, width, cell_size):
    for j in range(0, height, cell_size):
        b1 = Border(i, j, i + cell_size, j + 2)
        b2 = Border(i, j, i + 2, j + cell_size)
run = True
screen = pygame.display.set_mode((width, height))
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            f = open('maps/{}_level.txt'.format(number), 'w')
            for i in range(0, height, cell_size):
                f.write(''.join([str(j) for j in vert_borders[i // cell_size]]))
                f.write('\n')
            for i in range(0, height, cell_size):
                f.write(''.join([str(j) for j in hor_borders[i // cell_size]]))
                f.write('\n')
            f.close()
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            sprite = pygame.sprite.Sprite()
            sprite.rect = pygame.Rect(*pygame.mouse.get_pos(), 2, 2)
            collsion1 = pygame.sprite.spritecollide(sprite, vertical_borders, False)
            collsion2 = pygame.sprite.spritecollide(sprite, horizontal_borders, False)
            if collsion1:
                x = collsion1[0].rect.x // cell_size
                y = collsion1[0].rect.y // cell_size
                if vert_borders[y][x] == 0:
                    transf = 5
                    vert_borders[y][x] = 1
                else:
                    transf = 2
                    vert_borders[y][x] = 0
                collsion1[0].image = pygame.transform.scale(collsion1[0].image, (transf, cell_size))
            if collsion2:
                x = collsion2[0].rect.x // cell_size
                y = collsion2[0].rect.y // cell_size
                if hor_borders[y][x] == 0:
                    transf = 5
                    hor_borders[y][x] = 1
                else:
                    transf = 2
                    hor_borders[y][x] = 0
                collsion2[0].image = pygame.transform.scale(collsion2[0].image, (cell_size, transf))

    screen.fill((255, 255, 255))
    horizontal_borders.draw(screen)
    vertical_borders.draw(screen)
    pygame.display.flip()

pygame.quit()
