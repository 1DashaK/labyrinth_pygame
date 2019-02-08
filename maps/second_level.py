import pygame


class Border(pygame.sprite.Sprite):  # класс стен
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(borders_second_level)
        self.add(borders_second_level)
        self.image = pygame.Surface([abs(x2 - x1), abs(y2 - y1)])
        self.rect = pygame.Rect(x1, y1, abs(x2 - x1), abs(y2 - y1))


pygame.init()
size = width, height = 525, 675
screen = pygame.display.set_mode(size)

borders_second_level = pygame.sprite.Group()  # группа стен второго уровня

k = 75

Border(3 * k, k, 4 * k, k + 2)  # создаю горизонтальные стены лабиринта. первый слой
Border(k, 2 * k, 3 * k, 2 * k + 2)  # второй слой
Border(4 * k, 3 * k, 5 * k, 3 * k + 2)  # третий слой
Border(0, 4 * k, k, 4 * k + 2)  # четвертый слой
Border(3 * k, 4 * k, 6 * k, 4 * k + 2)
Border(5 * k, 5 * k, 7 * k, 5 * k + 2)  # пятый слой
Border(3 * k, 6 * k, 4 * k, 6 * k + 2)  # шестой слой
Border(5 * k, 6 * k, 6 * k, 6 * k + 2)
Border(4 * k, 7 * k, 5 * k, 7 * k + 2)  # седьмой слой
Border(k, 8 * k, 5 * k, 8 * k + 2)  # восьмой слой

Border(k, k, k + 2, 4 * k)  # создаю вертикальные стены лабиринта. первый столбец
Border(k, 5 * k, k + 2, 8 * k)
Border(2 * k, k, 2 * k + 2, 3 * k)  # второй столбец
Border(2 * k, 4 * k, 2 * k + 2, 6 * k)
Border(2 * k, 7 * k, 2 * k + 2, 8 * k)
Border(3 * k, 0, 3 * k + 2, k)  # третий столбец
Border(3 * k, 2 * k, 3 * k + 2, 4 * k)
Border(3 * k, 5 * k, 3 * k + 2, 8 * k)
Border(4 * k, k, 4 * k + 2, 2 * k)  # четвертый столбец
Border(4 * k, 4 * k, 4 * k + 2, 6 * k)
Border(5 * k, 0, 5 * k + 2, 3 * k)  # пятый столбец
Border(5 * k, 6 * k, 5 * k + 2, 7 * k)
Border(6 * k, k, 6 * k + 2, 4 * k)  # шестой столбец
Border(6 * k, 6 * k, 6 * k + 2, 9 * k)


Border(0, 0, width, 5)  # создание стен экрана
Border(0, height - 5, width, height)
Border(0, 0, 5, height)
Border(width - 5, 0, width, height)

if __name__ == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        borders_second_level.draw(screen)
        pygame.display.flip()
