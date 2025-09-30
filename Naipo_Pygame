import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((900, 660))    # Tamaño de la ventana
pygame.display.set_caption("Naipo")             # Nombre de la ventana
clock = pygame.time.Clock()                     # Para el manejo del framerate
running = True


# Bucle de juego:
while running:
    for event in pygame.event.get():            # Comprueba si se ha presionado X
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()