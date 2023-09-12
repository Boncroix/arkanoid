# estándar
import os

# librerías de terceros
import pygame as pg

# mis imports
from .import ALTO, ANCHO


class Raqueta(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.imagenes = []
        for i in range(3):
            ruta_image = os.path.join(
                'resources', 'images', f'electric0{i}.png')
            self.imagenes.append(pg.image.load(ruta_image))

        self.contador = 0
        self.image = self.imagenes[self.contador]

        margen = 25
        self.rect = self.image.get_rect(midbottom=(ANCHO/2, ALTO - margen))

    def update(self):
        # 00 -> 01 -> 02 -> 00 -> 01 -> 02
        self.contador += 1
        if self.contador > 2:
            self.contador = 0
        self.image = self.imagenes[self.contador]
