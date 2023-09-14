# estándar
import os
from typing import Any

# librerías de terceros
import pygame as pg
from random import choice, randint

# mis imports
from .import ALTO, ANCHO


class Raqueta(pg.sprite.Sprite):

    margen = 25
    vel_raqueta = 20

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
                self.rect.x -= self.vel_raqueta
        if estado_teclas[pg.K_RIGHT]:
            if self.rect.x >= ANCHO - self.rect.width:
                self.rect.x = ANCHO - self.rect.width
            else:
                self.rect.x += self.vel_raqueta


class Pelota:

    vel_pelota = 25

    def __init__(self, rect_raqueta):
        self.rect_raqueta = rect_raqueta
        self.juego_iniciado = False
        ruta_pelota = os.path.join('resources', 'images', 'ball1.png')
        self.pelota = pg.image.load(ruta_pelota)
        self.rect = self.pelota.get_rect(
            midbottom=(ANCHO/2, ALTO - Raqueta.margen - self.rect_raqueta.height))
        self.velocidad_x = choice([-self.vel_pelota, self.vel_pelota])
        self.velocidad_y = randint(-self.vel_pelota, -5)

    def mover(self):

        estado_teclas = pg.key.get_pressed()
        if estado_teclas[pg.K_a]:
            self.juego_iniciado = True
        if not self.juego_iniciado:
            self.rect.centerx = self.rect_raqueta.centerx
        else:
            self.rect.x += self.velocidad_x
            self.rect.y += self.velocidad_y
            if self.rect.y <= 0:
                self.rect.y = 0
                self.velocidad_y = -self.velocidad_y
            if self.rect.x <= 0:
                self.rect.x = 0
                self.velocidad_x = -self.velocidad_x
            if self.rect.x >= ANCHO - self.rect.width:
                self.rect.x = ANCHO - self.rect.width
                self.velocidad_x = -self.velocidad_x
