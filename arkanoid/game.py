import pygame as pg

from . import ALTO, ANCHO
from .escenas import MejoresJugadores, Partida, Portada


class Arkanoid:
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))

        # Escrito de forma abreviada
        # self.escenas = [
        #     Portada(self.pantalla),
        #     Partida(self.pantalla),
        #     MejoresJugadores(self.pantalla, partida.marcador)
        # ]

    def jugar(self):
        jugar_otra = True
        while jugar_otra:
            portada = Portada(self.pantalla)
            partida = Partida(self.pantalla)
            records = MejoresJugadores(self.pantalla, partida.marcador)

            self.escenas = [
                portada,
                partida,
                records
            ]

            for escena in self.escenas:
                he_acabado = escena.bucle_principal()
                jugar_otra = escena.jugar_otra
                if he_acabado:
                    print('La escena me pide que acabe el juego')
                    break
        print('He salido del bucle for de las escenas')

        pg.quit()


if __name__ == '__main__':
    print('Arrancamos desde el archivo game.py')
    juego = Arkanoid()
    juego.jugar()
