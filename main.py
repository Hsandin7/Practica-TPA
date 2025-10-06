# from Clases.jugador import Jugador
from Clases.carta import Carta
from Clases.boton import Boton
import pygame
import sys

# Inicializar pygame
pygame.init()

# VARIABLES
screen_width = 1280
screen_height = 720
pagina_actual = 0       # Páginas: 0: Menú principal, 1: Juego, 2: Salir

# Configuración de la ventana
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Naipo")
clock = pygame.time.Clock()

# Imágenes de fondo
menu_principal = pygame.image.load("Graficos/Menu_principal.png")
menu_juego = pygame.image.load("Graficos/Menú_Juego.jpg")
menu_salir = pygame.image.load("Graficos/Control_Salida.png").convert_alpha()

# Clases Boton
boton_play = Boton("Graficos/play.png", (560, 595))
boton_continuar = Boton("Graficos/Boton_Cont.png", (screen_width/2 - 210/2, 15))


##### TESTING CLASE CARTAS
cartas = []
pos_inicial_x = 535

for i in range(0,8):
    cartas.append(Carta(i+1, "o"))
    cartas[i].asignar_posicion(pos_inicial_x + 75*i, 500)
#####


while True:
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # --- Detectar tecla ESC solo en la página de juego ---
        if pagina_actual == 1 and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pagina_actual = 2  # Ir al menú de salida

    # --- Página principal ---
    if pagina_actual == 0:
        screen.blit(menu_principal, (0, 0))
        boton_play.dibujar(screen)

        if boton_play.detectar_click(eventos):
            print("¡Has pulsado PLAY!")
            pagina_actual = 1

    # --- Página del juego ---
    elif pagina_actual == 1:
        screen.blit(menu_juego, (0,0))
        
        ##### TESTING
        for carta in cartas:
            carta.mostrar(screen)
        #####


    # --- Página de salida ---
    elif pagina_actual == 2:
        screen.blit(menu_salir, (screen_width/2 - menu_salir.get_width()/2,0))
        boton_continuar.dibujar(screen)

        if boton_continuar.detectar_click(eventos):
            pagina_actual = 0

    pygame.display.flip()
    clock.tick(60)


