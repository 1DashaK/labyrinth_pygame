import pygame


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(borders_second_level)
        self.add(borders_second_level)
        self.image = pygame.Surface([abs(x2 - x1), abs(y2 - y1)])
        self.rect = pygame.Rect(x1, y1, abs(x2 - x1), abs(y2 - y1))
        print(x1, y1, x2, y2)


pygame.init()
size = width, height = 1000, 600
screen = pygame.display.set_mode(size)

borders_second_level = pygame.sprite.Group()

k = 37.5

Border(0, 0, width, 5)
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
