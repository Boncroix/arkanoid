# estándar
import os

# librerías de terceros
import pygame as pg

# mis imports
from .import ALTO, ANCHO


class Raqueta(pg.sprite.Sprite):

    margen = 25
    velocidad = 15

    def __init__(self):
        super().__init__()

        self.imagenes = []
        for i in range(3):
            ruta_image = os.path.join(
                'resources', 'images', f'electric0{i}.png')
            self.imagenes.append(pg.image.load(ruta_image))

        self.contador = 0
        self.image = self.imagenes[self.contador]

        self.rect = self.image.get_rect(
            midbottom=(ANCHO / 2, ALTO - self.margen))

    def update(self):
        # 00 -> 01 -> 02 -> 00 -> 01 -> 02
        self.contador += 1
        if self.contador > 2:
            self.contador = 0
        self.image = self.imagenes[self.contador]

        estado_teclas = pg.key.get_pressed()
        if estado_teclas[pg.K_LEFT]:
            if self.rect.x <= 0:
                self.rect.x = 0
            else:
                self.rect.x -= self.velocidad
        if estado_teclas[pg.K_RIGHT]:
            if self.rect.x >= ANCHO - self.rect.width:
                self.rect.x = ANCHO - self.rect.width
            else:
                self.rect.x += self.velocidad
