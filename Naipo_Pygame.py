import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la ventana
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Naipo")
clock = pygame.time.Clock()

# Páginas: 0 = Menú principal, 1 = Juego, 2 = Salir
pagina_actual = 0   

# Imagen de fondo del menú
menu_principal = pygame.image.load("Graficos/Menu_principal.png")

# Imagen de fondo del juego
menu_juego = pygame.image.load("Graficos/Menú_Juego.jpg")

# Imagen de salida
menu_salir = pygame.image.load("Graficos/Control_Salida.PNG")

# Imagen del botón play
boton2 = pygame.image.load("Graficos/play.png")

# Imagen del botón continuar
boton_continuar = pygame.image.load("Graficos/Boton_Cont.png")

# Crear rectángulos del botón con el tamaño de la imagen
boton_pos = boton2.get_rect(topleft=(559, 595))
boton_continuar_pos = boton_continuar.get_rect(topleft=(266, 52))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # --- Detectar tecla ESC solo en la página de juego ---
        if pagina_actual == 1:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pagina_actual = 2  # Ir al menú de salida

    # --- Página principal ---
    if pagina_actual == 0:
        screen.blit(menu_principal, (0, 0))

        # Detectar mouse
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if boton_pos.collidepoint(mouse):  # mouse encima del botón
            screen.blit(boton2, boton_pos.topleft)  # usar .topleft para blit

            if click[0] == 1:  # click izquierdo
                print("¡Has pulsado PLAY!")
                pagina_actual = 1

    # --- Página del juego ---
    elif pagina_actual == 1:
        screen.blit(menu_juego, (0,0))

    # --- Página de salida ---
    elif pagina_actual == 2:
        screen.blit(menu_salir, (550,0))
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if boton_continuar_pos.collidepoint(mouse):
            screen.blit(boton_continuar, boton_continuar_pos.topleft)
            
            if click[0] == 1:
                pagina_actual = 0

    pygame.display.flip()
    clock.tick(60)
