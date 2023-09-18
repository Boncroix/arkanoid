# estándar
import os
from typing import Any

# librerías de terceros
import pygame as pg
from random import choice, randint


# mis imports
from .import ALTO, ANCHO


class Raqueta(pg.sprite.Sprite):

    margen = 50
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

        self.rect1 = pg.Rect(self.rect.left, self.rect.top,
                             self.rect.width / 2, self.rect.height)
        self.rect2 = pg.Rect(self.rect.centerx, self.rect.top,
                             self.rect.width / 2, self.rect.height)

        # 00 -> 01 -> 02 -> 00 -> 01 -> 02
        self.contador += 1
        if self.contador > 2:
            self.contador = 0
        self.image = self.imagenes[self.contador]

        # Margenes para que la raqueta no se salga de la pantalla
        estado_teclas = pg.key.get_pressed()
        if estado_teclas[pg.K_LEFT]:
            self.rect.x -= self.vel_raqueta
            if self.rect.left < 0:
                self.rect.left = 0

        if estado_teclas[pg.K_RIGHT]:
            self.rect.x += self.vel_raqueta
            if self.rect.right > ANCHO:
                self.rect.right = ANCHO


class Pelota(pg.sprite.Sprite):

    vel_pelota = 20
    vidas = 3

    def __init__(self, raqueta):
        super().__init__()
        self.raqueta = raqueta
        ruta_pelota = os.path.join('resources', 'images', 'ball1.png')
        self.image = pg.image.load(ruta_pelota)
        self.rect = self.image.get_rect(midbottom=self.raqueta.rect.midtop)

    def update(self, juego_iniciado):

        if not juego_iniciado:
            self.rect = self.image.get_rect(midbottom=self.raqueta.rect.midtop)
            self.vel_x = choice([-self.vel_pelota, self.vel_pelota])
            self.vel_y = randint(-self.vel_pelota, -5)
            self.reset()
        else:
            self.rect.x += self.vel_x
            if self.rect.left <= 0 or self.rect.right > ANCHO:
                self.vel_x = -self.vel_x

            self.rect.y += self.vel_y
            if self.rect.top <= 0:
                self.vel_y = -self.vel_y

            if self.rect.top >= ALTO:
                self.pierdes()
                juego_iniciado = False
                return juego_iniciado

            self.hay_colision()

        return juego_iniciado

    def hay_colision(self):
        '''
        if self.rect.colliderect(self.raqueta.rect1):
            self.vel_y = -self.vel_pelota
            self.vel_x = randint(-self.vel_pelota, 0)
        if self.rect.colliderect(self.raqueta.rect2):
            self.vel_y = -self.vel_pelota
            self.vel_x = randint(0, self.vel_pelota)
        '''

        if pg.sprite.collide_mask(self, self.raqueta):
            self.vel_y = -self.vel_pelota
            self.vel_x = randint(-self.vel_pelota,
                                 self.vel_pelota)

    def pierdes(self):
        self.restar_vida = True
        self.vidas -= 1

    def reset(self):
        self.restar_vida = False


class Ladrillo(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        ruta_verde = os.path.join('resources', 'images', 'greenTile.png')
        self.image = pg.image.load(ruta_verde)
        self.rect = self.image.get_rect()

    def undate(self):
        pass


class IndicadorVida(pg.sprite.Sprite):
    borde = 20
    escala_x = 57
    escala_y = 15

    def __init__(self):
        super().__init__()
        self.imagenes = []
        for i in range(3):
            ruta_image = os.path.join(
                'resources', 'images', f'electric0{i}.png')
            self.image = pg.image.load(ruta_image)
            self.image = pg.transform.scale(
                self.image, (self.escala_x, self.escala_y))
            self.imagenes.append(self.image)

        self.contador = 0
        self.rect = self.image.get_rect()
        self.image = self.imagenes[self.contador]

    def update(self):
        # 00 -> 01 -> 02 -> 00 -> 01 -> 02
        self.contador += 1
        if self.contador > 2:
            self.contador = 0
        self.image = self.imagenes[self.contador]
