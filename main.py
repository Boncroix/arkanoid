from arkanoid import ALTO, ANCHO
from arkanoid.game import Arkanoid

if __name__ == '__main__': 
    print(
        f'Arrancamos desde el archivo main.py y la pantalla es de tamaño {ANCHO}x{ALTO}')
    juego = Arkanoid()
    juego.jugar()
