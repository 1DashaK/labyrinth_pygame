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

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

pygame.init()
size = width, height = 1000, 600
screen = pygame.display.set_mode(size)

all_sprites = pygame.sprite.Group()
sprite_l_1 = pygame.sprite.Sprite(all_sprites)
image = load_image("Run_Left_1.png")
sprite_l_1.image = image
sprite_l_2 = pygame.sprite.Sprite(all_sprites)
sprite_l_2.image = load_image("Run_Left_2.png")
sprite_l_3 = pygame.sprite.Sprite(all_sprites)
sprite_l_3.image = load_image("Run_Left_3.png")
sprite_l_4 = pygame.sprite.Sprite(all_sprites)
sprite_l_4.image = load_image("Run_Left_4.png")
sprite_r_1 = pygame.sprite.Sprite(all_sprites)
sprite_r_1.image = load_image("Run_Right_1.png")
sprite_r_2 = pygame.sprite.Sprite(all_sprites)
sprite_r_2.image = load_image("Run_Right_2.png")
sprite_r_3 = pygame.sprite.Sprite(all_sprites)
sprite_r_3.image = load_image("Run_Right_3.png")
sprite_r_4 = pygame.sprite.Sprite(all_sprites)
sprite_r_4.image = load_image("Run_Right_4.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.display.flip()
