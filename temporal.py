import pygame
import sys

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))    # Tamaño de la ventana
pygame.display.set_caption("Naipo")             # Nombre de la ventana
clock = pygame.time.Clock()                     # Para el manejo del framerate



color = (255, 192, 203)  



# Bucle de juego:
while True:
    for event in pygame.event.get():            # Comprueba si se ha presionado X
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((100,100,100))

    pygame.draw.rect(screen, color, pygame.Rect(30, 30, 5, 5))  

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

