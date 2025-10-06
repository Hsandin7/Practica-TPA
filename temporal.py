# from Clases.jugador import Jugador
from Clases.carta import Carta
from Clases.boton import Boton
import pygame
import sys

# Inicializar pygame
pygame.init()

# VARIABLES
ancho_pantalla = 1280
alto_pantalla = 720
pagina_actual = 0       # Páginas: 0: Menú principal, 1: Juego, 2: Salir

# Configuración de la ventana
screen = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Naipo")
clock = pygame.time.Clock()

# --- IMÁGENES DE FONDO ---
menu_principal = pygame.image.load("Graficos/Menu_principal.png")
menu_juego = pygame.image.load("Graficos/Menú_Juego.jpg")
menu_salir = pygame.image.load("Graficos/Control_Salida.PNG")

# --- BOTONES ---
boton_play = Boton("Graficos/play.jpg", (559, 595))
boton_continuar = Boton("Graficos/Boton_Cont.PNG", (266, 52))

# --- CARTAS (solo para testeo visual) ---
cartas = []
pos_inicial_x = 535
for i in range(8):
    cartas.append(Carta(i + 1, "o"))
    cartas[i].asignar_posicion(pos_inicial_x + 75 * i, 500)

# --- BUCLE PRINCIPAL ---
while True:
    eventos = pygame.event.get()

    for event in eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # --- Detectar tecla ESC solo en la página de juego ---
        if pagina_actual == 1 and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pagina_actual = 2  # Ir al menú de salida

    # --- PÁGINA PRINCIPAL ---
    if pagina_actual == 0:
        screen.blit(menu_principal, (0, 0))
        boton_play.dibujar(screen)

        if boton_play.detectar_click(eventos):
            print("¡Has pulsado PLAY!")
            pagina_actual = 1

    # --- PÁGINA DEL JUEGO ---
    elif pagina_actual == 1:
        screen.blit(menu_juego, (0, 0))

        # Mostrar cartas (solo test)
        for carta in cartas:
            carta.mostrar(screen)

    # --- PÁGINA DE SALIDA ---
    elif pagina_actual == 2:
        screen.blit(menu_salir, (550, 0))
        boton_continuar.dibujar(screen)

        if boton_continuar.detectar_click(eventos):
            pagina_actual = 0

    # --- ACTUALIZAR PANTALLA ---
    pygame.display.flip()
    clock.tick(60)
