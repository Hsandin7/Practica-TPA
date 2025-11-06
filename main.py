import sys
import pygame
from src.juego import Juego
from src.animaciones import Transicion
from src.demo import Demo

# Inicializar pygame
pygame.init()

# Configuración de la ventana
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Naipo")
clock = pygame.time.Clock()

# Creación del Juego
juego = Juego()
transicion = Transicion()
demo = Demo()

while True:
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # --- Detectar tecla ESC ---
        if Juego.num_transicion is None and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            juego.mostrar_fondo = True
            match juego.pagina_actual:
                case 0:                         # P Principal
                    pygame.quit()                   # -> Cerrar el juego
                    sys.exit()
                case 1 | 4:                     # P Juego / M Guardado
                    juego.pagina_actual = 2         # -> M Salida
                case 2 | 3 | 6:                 # M Salida / M Tienda / M Info
                    juego.pagina_actual = 1         # -> P Juego
                case _:
                    pass

    # Manejo de transiciones
    if Juego.num_transicion:
        num_pagina_destino = transicion.actualizar(screen)
        if num_pagina_destino is not None:
            juego.pagina_actual = num_pagina_destino
            Juego.num_transicion = None
    
    # Ejecucion de la demo
    elif demo.activa:
        demo.ejecutar_demo(screen, juego, transicion, eventos)

    
    # Manejo de las paginas
    else:
        if juego.pagina_actual == 0: demo.checkear_inicio()
        else: demo.contador = 0
        
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
                juego.mostrar_menu_tienda(screen)
                juego.actualizar_menu_tienda(eventos)
            case 4:
                juego.mostrar_menu_guardado(screen)
                juego.actualizar_menu_guardado(eventos)
            case 5:
                juego.mostrar_pagina_game_over(screen)
                juego.actualizar_pagina_game_over(eventos)
            case 6: 
                juego.mostrar_pantalla_info(screen)


        if Juego.num_transicion:
            transicion.iniciar(*Juego.paginas_transicion, Juego.num_transicion)

    pygame.display.flip()
    clock.tick(60)


