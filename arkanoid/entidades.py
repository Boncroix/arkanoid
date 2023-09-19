# estándar
import os
from typing import Any

# librerías de terceros
import pygame as pg
from random import choice, randint


# mis imports
from .import ALTO, ALTO_MARCADOR, ANCHO


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

    def __init__(self, raqueta):
        super().__init__()
        self.raqueta = raqueta
        ruta_pelota = os.path.join('resources', 'images', 'ball1.png')
        self.image = pg.image.load(ruta_pelota)
        self.rect = self.image.get_rect(midbottom=self.raqueta.rect.midtop)
        self.he_perdido = False

    def update(self, juego_iniciado):

        if not juego_iniciado:
            self.rect = self.image.get_rect(midbottom=self.raqueta.rect.midtop)
            self.vel_x = choice([-self.vel_pelota, self.vel_pelota])
            self.vel_y = randint(-self.vel_pelota, -5)
            self.he_perdido = False

        else:
            self.rect.x += self.vel_x
            self.rect.y += self.vel_y

            if self.rect.left <= 0 or self.rect.right > ANCHO:
                self.vel_x = -self.vel_x

            if self.rect.top <= ALTO_MARCADOR:
                self.vel_y = -self.vel_y

            if self.rect.top >= ALTO:
                self.he_perdido = True

            self.hay_colision()

    def hay_colision(self):

        if pg.sprite.collide_mask(self, self.raqueta):
            self.vel_y = -self.vel_pelota
            if self.rect.centerx > self.raqueta.rect.centerx:
                self.vel_x = randint(0, self.vel_pelota)
            elif self.rect.centerx < self.raqueta.rect.centerx:
                self.vel_x = randint(-self.vel_pelota, 0)
            else:
                self.vel_x = 0

        '''
        if self.rect.colliderect(self.raqueta.rect1):
            self.vel_y = -self.vel_pelota
            self.vel_x = randint(-self.vel_pelota, 0)
        if self.rect.colliderect(self.raqueta.rect2):
            self.vel_y = -self.vel_pelota
            self.vel_x = randint(0, self.vel_pelota)
        '''

        '''

        if pg.sprite.collide_mask(self, self.raqueta):
            self.vel_y = -self.vel_pelota
            self.vel_x = randint(-self.vel_pelota,
                                 self.vel_pelota)
            
        '''

    def pierdes(self):
        pass

    def reset(self):
        pass


class Ladrillo(pg.sprite.Sprite):
    VERDE = 0
    ROJO = 1
    ROJO_ROTO = 2
    IMG_LADRILLO = ['greenTile.png', 'redTile.png', 'redTileBreak.png']

    def __init__(self, puntos, color=VERDE):
        super().__init__()
        self.tipo = color
        self.imagenes = []
        for img in self.IMG_LADRILLO:
            ruta = os.path.join(
                'resources', 'images', img)
            self.imagenes.append(pg.image.load(ruta))
        self.image = self.imagenes[color]
        self.rect = self.image.get_rect()
        self.puntos = puntos

    def update(self, muro):
        '''
        Según tipo de ladrillo devolvemos True o False si el ladrillo se rompe
        '''
        if self.tipo == Ladrillo.ROJO:
            self.tipo = Ladrillo.ROJO_ROTO
            self.image = self.imagenes[self.tipo]
            return False
        else:
            muro.remove(self)
            return True


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


class ContadorVidas:
    def __init__(self, vidas_iniciales):
        self.vidas = vidas_iniciales

    def perder_vida(self):
        self.vidas -= 1
        return self.vidas == 0

    def pintar(self):
        pass


class Marcador:
    def __init__(self):
        self.valor = 0
        fuente = 'LibreFranklin-VariableFont_wght.ttf'
        ruta = os.path.join('resources', 'fonts', fuente)
        self.tipografia = pg.font.Font(ruta, 35)

    def aumentar(self, incremento):
        self.valor += incremento

    def pintar(self, pantalla):
        r = pg.rect.Rect(0, 0, ANCHO, ALTO_MARCADOR)
        pg.draw.rect(pantalla, (0, 0, 0), r)
        cadena = str(self.valor)
        texto = self.tipografia.render(cadena, True, (230, 189, 55))
        pos_x = 20
        pos_y = 10
        pantalla.blit(texto, (pos_x, pos_y))

        # TODO: acciones para pintar el marcador en pantalla
