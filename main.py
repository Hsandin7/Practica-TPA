# from Clases.jugador import Jugador
from Clases.juego import Juego
from Clases.animaciones import Transicion
import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la ventana
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Naipo")
clock = pygame.time.Clock()

# Creación del Juego
juego = Juego()
transicion = Transicion()

while True:
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # --- Detectar tecla ESC solo en la página de juego ---
        if juego.pagina_actual == 1 and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            juego.pagina_actual = 2  # Ir al menú de salida

    if Juego.transicion:
        num = transicion.actualizar(screen)
        if num is not None:
            juego.pagina_actual = num
            Juego.transicion = False
    else:
        match juego.pagina_actual:
            case 0:
                juego.mostrar_pagina_principal(screen)
                juego.actualizar_pagina_principal(eventos)
            case 1:
                juego.mostrar_pagina_juego(screen)
                juego.actualizar_pagina_juego(eventos)
            case 2:
                juego.mostrar_menu_salida(screen)
                juego.actualizar_menu_salida(eventos)
            case 3:
                juego.mostrar_Tienda(screen)
                juego.actualizar_Tienda(eventos)
            case _:
                pass

        if Juego.transicion:
            transicion.iniciar(Juego.paginas_transicion[0],
                               Juego.paginas_transicion[1],
                               Juego.paginas_transicion[2])

    pygame.display.flip()
    clock.tick(60)


