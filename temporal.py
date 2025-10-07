# from Clases.jugador import Jugador
from Clases.juego import Juego
import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la ventana
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Naipo")
clock = pygame.time.Clock()

# Creación del Juego
juego = Juego(screen)
juego._cargar_imagenes()

while True:
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # --- Detectar tecla ESC solo en la página de juego ---
        if juego.pagina_actual == 1 and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            juego.pagina_actual = 2  # Ir al menú de salida

    match juego.pagina_actual:
        case 0:
            juego.mostrar_pagina_principal(eventos)
        case 1:
            juego.mostrar_pagina_juego(eventos)
        case 2:
            juego.mostrar_menu_salida(eventos)
        case 3:
            pass # Nueva ventana

    pygame.display.flip()
    clock.tick(60)


