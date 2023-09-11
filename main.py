from arkanoid import ALTO, ANCHO
from arkanoid.game import Arkanoid


if __name__ == '__main__':
    print(
        'Arrancamos desde el archovo main.py y la pantalla es de tamaño {ANCHO}X{ALTO}')
    juego = Arkanoid()
    juego.jugar()
