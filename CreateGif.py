import pygame
from LooseImgLoader import GifLoader

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, path):
        super().__init__()
        self.sprites = GifLoader(path)
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def update(self, speed):
        self.current_sprite += speed
        if int(self.current_sprite) >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]