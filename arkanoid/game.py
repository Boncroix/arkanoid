import pygame

# CONSTANTES PANTALLA
ALTO = 600
ANCHO = 800
COLOR_FONDO = (99, 0, 0)


class Arkanoid():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Arkanoid')
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))

    def jugar(self):
        salir = False
        while not salir:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT or (evento.type == pygame.KEYUP and evento.key == pygame.K_ESCAPE):
                    salir = True
            # 2. Calcular estado de elementos y pintarlos
            self.pantalla.fill(COLOR_FONDO)
            # 3. ostrar los cambios (pintados) y controlar el reloj
            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    print('Arrancamos desde el archivo game.py')
    juego = Arkanoid()
    juego.jugar

