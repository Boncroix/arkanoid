# librerias estándar        orden de las librerias
import os

# librerias de terceros
import pygame as pg

# tus dependencias librerias creadas por nosotros
from . import ANCHO, ALTO


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla

    def bucle_principal(self):
        '''
        Este método debe ser implementado por todas y cada una de las escenas,
        en función de lo que estén esperando hata la condición de salida.
        '''

        pass


class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        # windows: resources\images\arkanoid_name.png
        # mac/linux: resource/images/arkanoid_name.png   os.path.join selecciona las barras independientemente del sistema operativo
        ruta = os.path.join('resources', 'images', 'arkanoid_name.png')
        self.logo = pg.image.load(ruta)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True
            self.pantalla.fill((99, 0, 0))
            self.pintar_logo()
            pg.display.flip()

    def pintar_logo(self):
        ancho, alto = self.logo.get_size()
        pos_x = (ANCHO - ancho) / 2
        pos_y = (ALTO - alto) / 2
        self.pantalla.blit(
            self.logo, (pos_x, pos_y))


class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True
            self.pantalla.fill((0, 99, 0))
            pg.display.flip()


class MejoresJugadores(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True
            self.pantalla.fill((0, 0, 99))
            pg.display.flip()
