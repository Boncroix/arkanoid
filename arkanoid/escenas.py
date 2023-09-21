# estándar
import os

# librerías de terceros
import pygame as pg
from random import randint, choice

# tus dependencias
from . import ALTO, ANCHO, COLOR_FONDO, FPS, VIDAS
from .entidades import (ContadorVidas,
                        IndicadorVida, Ladrillo, Marcador, Pelota, Raqueta
                        )


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
        self.contador_vidas = ContadorVidas(VIDAS)
        self.crear_vidas(VIDAS)
        self.marcador = Marcador()

    def bucle_principal(self):
        super().bucle_principal()
        print('Estamos en el bucle principal de PARTIDA')
        salir = False
        juego_iniciado = False
        restar_vida = False
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
            self.pelota.update(juego_iniciado)
            self.pantalla.blit(self.pelota.image, self.pelota.rect)
            self.muro.draw(self.pantalla)
            self.indicador_vidas.update()
            self.indicador_vidas.draw(self.pantalla)
            self.detectar_colision_muro()
            self.marcador.pintar(self.pantalla)

            pg.display.flip()

            if self.pelota.he_perdido:
                restar_vida = False
                salir = self.contador_vidas.perder_vida()
                self.restar_vida()
                self.pelota.he_perdido = False
                juego_iniciado = False

    def detectar_colision_muro(self):
        golpeados = pg.sprite.spritecollide(self.pelota, self.muro, False)
        if len(golpeados) > 0:
            for ladrillo in golpeados:
                if ladrillo.update(self.muro):
                    self.marcador.aumentar(ladrillo.puntos)

            self.pelota.vel_y = -self.pelota.vel_y

    def pintar_fondo(self):
        ajuste_imagen = 10

        self.pantalla.fill(COLOR_FONDO)
        # TODO: mejorar la lógica para 'rellenar' el fondo
        self.pantalla.blit(self.fondo, (0, 0))
        if ANCHO > self.fondo.get_width():
            self.pantalla.blit(self.fondo, (self.fondo.get_width(), 0))
        if ALTO > self.fondo.get_height():
            self.pantalla.blit(
                self.fondo, (0, self.fondo.get_height() - ajuste_imagen))
            self.pantalla.blit(
                self.fondo, (self.fondo.get_width(), self.fondo.get_height() - ajuste_imagen))

    def crear_muro(self):
        filas = 6
        columnas = 7
        margen_superior = 60
        tipo = None

        for fila in range(filas):   # 0-3
            for col in range(columnas):
                # por aquí voy a pasar filas*columnas = 24 veces
                if tipo == Ladrillo.ROJO:
                    tipo = Ladrillo.VERDE
                else:
                    tipo = Ladrillo.ROJO
                puntos = (tipo+1)*(20-fila*2)
                ladrillo = Ladrillo(puntos, tipo)
                margen_izquierdo = (ANCHO - columnas * ladrillo.rect.width) / 2
                # x = ancho_lad * col
                # y = alto_lad * fila
                ladrillo.rect.x = ladrillo.rect.width * col + margen_izquierdo
                ladrillo.rect.y = ladrillo.rect.height * fila + margen_superior
                self.muro.add(ladrillo)

    def crear_vidas(self, vidas):
        borde = 30
        separador = 5

        for vida in range(vidas):

            indicador = IndicadorVida()
            indicador.rect.x = indicador.rect.width * vida + borde + separador * vida
            indicador.rect.y = ALTO - borde
            self.indicador_vidas.add(indicador)

    def restar_vida(self):
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
