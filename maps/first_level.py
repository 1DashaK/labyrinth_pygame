import pygame


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(borders_first_level)
        self.add(borders_first_level)
        self.image = pygame.Surface([abs(x2 - x1), abs(y2 - y1)])
        self.rect = pygame.Rect(x1, y1, abs(x2 - x1), abs(y2 - y1))


pygame.init()
size = width, height = 525, 675
screen = pygame.display.set_mode(size)

borders_first_level = pygame.sprite.Group()

Border(0, 0, width, 5)  # создаю граничные стены экрана
Border(0, height - 5, width, height)
Border(0, 0, 5, height)
Border(width - 5, 0, width, height)

k = 37.5
Border(0, k, 4 * k, k + 2)  # создаю горизонтальные стены лабиринта. первый слой
Border(5 * k, k, 10 * k, k + 2)
Border(11 * k, k, 12 * k, k + 2)
Border(k, 2 * k, 5 * k, 2 * k + 2)  # второй слой
Border(6 * k, 2 * k, 11 * k, 2 * k + 2)
Border(0, 3 * k, 4 * k, 3 * k + 2)  # третий слой
Border(7 * k, 3 * k, 12 * k, 3 * k + 2)
Border(k, 4 * k, 5 * k, 4 * k + 2)  # четвертый слой
Border(6 * k, 4 * k, 7 * k, 4 * k + 2)
Border(8 * k, 4 * k, 9 * k, 4 * k + 2)
Border(10 * k, 4 * k, 11 * k, 4 * k + 2)
Border(13 * k, 4 * k, 14 * k, 4 * k + 2)
Border(0, 5 * k, 4 * k, 5 * k + 2)  # пятый слой
Border(5 * k, 5 * k, 6 * k, 5 * k + 2)
Border(7 * k, 5 * k, 8 * k, 5 * k + 2)
Border(10 * k, 5 * k, 11 * k, 5 * k + 2)
Border(k, 6 * k, 5 * k, 6 * k + 2)  # шестой слой
Border(0, 7 * k, 5 * k, 7 * k + 2)  # седьмой слой
Border(7 * k, 7 * k, 8 * k, 7 * k + 2)
Border(9 * k, 7 * k, 10 * k, 7 * k + 2)
Border(k, 17 * k, 5 * k, 17 * k + 2)  # семнадцатый слой
Border(6 * k, 17 * k, 13 * k, 17 * k + 2)
Border(k, 8 * k, 3 * k, 8 * k + 2)  # восьмой слой
Border(7 * k, 8 * k, 9 * k, 8 * k + 2)
Border(11 * k, 8 * k, 12 * k, 8 * k + 2)
Border(0, 9 * k, 2 * k, 9 * k + 2)  # девятый слой
Border(5 * k, 9 * k, 9 * k, 9 * k + 2)
Border(2 * k, 10 * k, 3 * k, 10 * k + 2)  # десятый слой
Border(4 * k, 10 * k, 5 * k, 10 * k + 2)
Border(10 * k, 10 * k, 11 * k, 10 * k + 2)
Border(3 * k, 11 * k, 4 * k, 11 * k + 2)  # одиннадцатый слой
Border(5 * k, 11 * k, 8 * k, 11 * k + 2)
Border(11 * k, 11 * k, 12 * k, 11 * k + 2)
Border(3 * k, 12 * k, 4 * k, 12 * k + 2)  # двенадцатый слой
Border(5 * k, 12 * k, 7 * k, 12 * k + 2)
Border(10 * k, 12 * k, 11 * k, 12 * k + 2)
Border(k, 13 * k, 3 * k, 13 * k + 2)  # тринадцатый слой
Border(6 * k, 13 * k, 8 * k, 13 * k + 2)
Border(k, 14 * k, 4 * k, 14 * k + 2)  # четырнадцатый слой
Border(5 * k, 14 * k, 9 * k, 14 * k + 2)
Border(11 * k, 14 * k, 12 * k, 14 * k + 2)
Border(k, 15 * k, 13 * k, 15 * k + 2)  # пятнадцатый слой
Border(3 * k, 16 * k, 8 * k, 16 * k + 2)  # шестнадцатый слой
Border(9 * k, 16 * k, 13 * k, 16 * k + 2)  # шестнадцатый слой


Border(k, 9 * k, k + 2, 13 * k)  # создаю вертикальные стены лабиринта. первый столбец
Border(k, 15 * k, k + 2, 17 * k)
Border(2 * k, 10 * k, 2 * k + 2, 13 * k)  # второй столбец
Border(3 * k, 8 * k, 3 * k + 2, 10 * k)  # третий столбец
Border(3 * k, 11 * k, 3 * k + 2, 12 * k)
Border(4 * k, 8 * k, 4 * k + 2, 11 * k)  # четвертый столбец
Border(4 * k, 12 * k, 4 * k + 2, 14 * k)
Border(5 * k, 2 * k, 5 * k + 2, 6 * k)  # пятый столбец
Border(5 * k, 7 * k, 5 * k + 2, 9 * k)
Border(5 * k, 10 * k, 5 * k + 2, 11 * k)
Border(5 * k, 12 * k, 5 * k + 2, 14 * k)
Border(6 * k, 2 * k, 6 * k + 2, 8 * k)  # шестой столбец
Border(6 * k, 9 * k, 6 * k + 2, 10 * k)
Border(6 * k, 11 * k, 6 * k + 2, 12 * k)
Border(6 * k, 17 * k, 6 * k + 2, 18 * k)
Border(7 * k, 3 * k, 7 * k + 2, 4 * k)  # седьмой столбец
Border(7 * k, 5 * k, 7 * k + 2, 7 * k)
Border(7 * k, 8 * k, 7 * k + 2, 9 * k)
Border(7 * k, 10 * k, 7 * k + 2, 11 * k)
Border(8 * k, 4 * k, 8 * k + 2, 5 * k)  # восьмой столбец
Border(8 * k, 6 * k, 8 * k + 2, 7 * k)
Border(8 * k, 9 * k, 8 * k + 2, 10 * k)
Border(8 * k, 11 * k, 8 * k + 2, 13 * k)
Border(8 * k, 16 * k, 8 * k + 2, 17 * k)
Border(9 * k, 3 * k, 9 * k + 2, 4 * k)  # девятый столбец
Border(9 * k, 5 * k, 9 * k + 2, 8 * k)
Border(9 * k, 9 * k, 9 * k + 2, 14 * k)
Border(9 * k, 15 * k, 9 * k + 2, 16 * k)
Border(10 * k, 3 * k, 10 * k + 2, 4 * k)  # десятый столбец
Border(10 * k, 5 * k, 10 * k + 2, 14 * k)
Border(10 * k, 0, 10 * k + 2, k)
Border(11 * k, 4 * k, 11 * k + 2, 8 * k)  # одиннадцатый столбец
Border(11 * k, k, 11 * k + 2, 2 * k)
Border(11 * k, 9 * k, 11 * k + 2, 10 * k)
Border(11 * k, 13 * k, 11 * k + 2, 14 * k)
Border(12 * k, 2 * k, 12 * k + 2, 6 * k)  # двенадцатый столбец
Border(12 * k, 7 * k, 12 * k + 2, 14 * k)
Border(13 * k, k, 13 * k + 2, 15 * k)  # тринадцатый столбец


if __name__ == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        borders_first_level.draw(screen)
        pygame.display.flip()
