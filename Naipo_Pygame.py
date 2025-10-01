import pygame
import sys

# pygame setup
pygame.init()
screen = pygame.display.set_mode((900, 660))    # Tamaño de la ventana
pygame.display.set_caption("Naipo")             # Nombre de la ventana
clock = pygame.time.Clock()                     # Para el manejo del framerate

# Variables
pagina_actual = 0       # 0) Pagina principal   1) 


font_test = pygame.font.Font("Testing.ttf", 100)

texto = font_test.render("ABCDEFGH", True, (255,255,255))

def boton():
    pass


class Carta:
    def __init__(self):
        pass







# Bucle de juego:
while True:
    for event in pygame.event.get():            # Comprueba si se ha presionado X
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((100,100,100))

    # RENDER YOUR GAME HERE
    screen.blit(texto, (10, 100))       # El .blit permite superponer cualquier cosa por encima de otra

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

