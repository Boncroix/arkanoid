import pygame

# CONSTANTES PANTALLA
ALTO = 600
ANCHO = 800


class Arkanoid():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Arkanoid')
        self.clock = pygame.time.Clock()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))

    def jugar(self):
        salir = False
        while not salir:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT or (evento.type == pygame.KEYUP and evento.key == pygame.K_ESCAPE):
                    salir = True

        pygame.quit()


if __name__ == '__main__':
    print('Estas llamando a Arkanoid desde la línea de comandos')
    juego = Arkanoid()
    juego.jugar
else:
    print('Estas llamando a Arkanoid desde una sentencia import')
    print(f'El nombre del paquete ahora es {__name__}')
