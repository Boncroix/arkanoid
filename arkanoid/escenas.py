# estándar
import os

# librerías de terceros
import pygame as pg

# tus dependencias
from . import ALTO, ANCHO


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla

    def bucle_principal(self):
        """
        Este método debe ser implementado por todas y cada una de las escenas,
        en función de lo que estén esperando hasta la condición de salida.
        """
        print('Método vacío bucle principal de ESCENA')


class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        # windows: resources\images\arkanoid_name.png
        # mac/linux: resources/images/arkanoid_name.png
        ruta = os.path.join('resources', 'images', 'arkanoid_name.png')
        self.logo = pg.image.load(ruta)

        ruta = os.path.join('resources', 'fonts', 'CabinSketch-Bold.ttf')
        self.tipo = pg.font.Font(ruta, 35)

    def bucle_principal(self):
        super().bucle_principal()
        print('Estamos en el bucle principal de PORTADA')
        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True
                if evento.type == pg.KEYDOWN and evento.key == pg.K_SPACE:
                    salir = True
            self.pantalla.fill((99, 0, 0))
            self.pintar_logo()
            self.pintar_mensaje()
            pg.display.flip()
        return False

    def pintar_logo(self):
        ancho, alto = self.logo.get_size()
        pos_x = (ANCHO - ancho) / 2
        pos_y = (ALTO - alto) / 2
        self.pantalla.blit(self.logo, (pos_x, pos_y))

    def pintar_mensaje(self):
        mensaje = "Pulsa <ESPACIO> para comenzar la partida"
        texto = self.tipo.render(mensaje, True, (255, 255, 255))
        pos_x = (ANCHO - texto.get_width()) / 2
        pos_y = ALTO * 3 / 4
        self.pantalla.blit(texto, (pos_x, pos_y))


class Partida(Escena):
    def bucle_principal(self):
        super().bucle_principal()
        print('Estamos en el bucle principal de PARTIDA')
        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True
            self.pantalla.fill((0, 99, 0))
            pg.display.flip()


class MejoresJugadores(Escena):
    def bucle_principal(self):
        super().bucle_principal()
        print('Estamos en el bucle principal de MEJORESJUGADORES')
        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True
            self.pantalla.fill((0, 0, 99))
            pg.display.flip()
