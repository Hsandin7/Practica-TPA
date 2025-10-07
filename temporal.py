import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Demo de transparencia")

# Cargar imágenes
fondo = pygame.image.load("Graficos/Menú_Juego.png") #.convert()  # Fondo sin transparencia
superior = pygame.image.load("Graficos/Control_Salida.png").convert_alpha()  # Con canal alpha

# Escalar imágenes al tamaño de la ventana (opcional)
# fondo = pygame.transform.scale(fondo, (0,0))
# superior = pygame.transform.scale(superior, (0,0))

# # Crear una versión translúcida del sprite superior
# superior_translucida = superior.copy()
# superior_translucida.set_alpha(255)  # 0 = invisible, 255 = opaco

# Posición del sprite superior
# x, y = (ANCHO - superior.get_width()) // 2, (ALTO - superior.get_height()) // 2

# Bucle principal
clock = pygame.time.Clock()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dibujar fondo
    ventana.blit(fondo, (0, 0))

    # Dibujar imagen translúcida encima
    ventana.blit(superior, (0, 0))

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)
