# estándar
import os

# librerías de terceros
import pygame as pg
from random import randint, choice

# tus dependencias
from . import ALTO, ANCHO, FPS
from .entidades import IndicadorVida, Ladrillo, Pelota, Raqueta


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

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
    def __init__(self, pantalla):
        super().__init__(pantalla)

        ruta_fondo = os.path.join('resources', 'images', 'background.jpg')
        self.fondo = pg.image.load(ruta_fondo)
        self.jugador = Raqueta()
        self.muro = pg.sprite.Group()
        self.crear_muro()
        self.pelota = Pelota(self.jugador)
        self.indicador_vidas = pg.sprite.Group()
        self.crear_vidas(self.pelota.vidas)

    def bucle_principal(self):
        super().bucle_principal()
        print('Estamos en el bucle principal de PARTIDA')
        salir = False
        juego_iniciado = False
        while not salir:
            self.reloj.tick(FPS)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True
                if evento.type == pg.KEYDOWN and evento.key == pg.K_SPACE:
                    juego_iniciado = True
            self.pintar_fondo()
            self.jugador.update()
            self.pantalla.blit(self.jugador.image, self.jugador.rect)
            juego_iniciado = self.pelota.update(juego_iniciado)
            self.restar_vida(self.pelota.restar_vida)
            self.comprobar_colision()
            self.pantalla.blit(self.pelota.image, self.pelota.rect)
            self.muro.draw(self.pantalla)
            self.indicador_vidas.update()
            self.indicador_vidas.draw(self.pantalla)
            pg.display.flip()

    def comprobar_colision(self):
        if self.pelota.rect.colliderect(self.jugador.rect):
            self.pelota.vel_y = randint(-self.pelota.vel_pelota, -5)
            self.pelota.vel_x = choice(
                [-self.pelota.vel_pelota, self.pelota.vel_pelota])

    def pintar_fondo(self):
        self.pantalla.fill((0, 0, 99))
        # TODO: mejorar la lógica para 'rellenar' el fondo
        self.pantalla.blit(self.fondo, (0, 0))
        self.pantalla.blit(self.fondo, (600, 0))

    def crear_muro(self):
        filas = 8
        columnas = 6
        margen_superior = 25
        ladrillo = Ladrillo()
        margen_inzquierdo = (ANCHO - columnas *
                             ladrillo.rect.width) / 2

        for fila in range(filas):
            for col in range(columnas):
                ladrillo = Ladrillo()
                ladrillo.rect.x = ladrillo.rect.width * col + margen_inzquierdo
                ladrillo.rect.y = ladrillo.rect.height * fila + margen_superior
                self.muro.add(ladrillo)

    def crear_vidas(self, vidas):
        borde = 30

        for vida in range(vidas):
            indicador = IndicadorVida()
            indicador.rect.x = indicador.rect.width * vida + borde
            indicador.rect.y = ALTO - borde
            self.indicador_vidas.add(indicador)

    def restar_vida(self, restar_vida):
        if restar_vida:
            self.indicador_vidas.sprites()[-1].kill()


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
