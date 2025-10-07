import pygame

class Boton:
    def __init__(self, ruta_imagen, posicion):
        self.imagen_original = pygame.image.load(ruta_imagen).convert_alpha()   # Carga la imagen
        self.rect = self.imagen_original.get_rect(topleft=posicion)             # Crea el rect correspondiente
        self.sonido_click = None                                                # Sonido para el click (Por hacer)

        # Crea una versión oscurecida de la imagen, usando multiplicación RGBA
        self.imagen_hover = self.imagen_original.copy()
        oscuridad = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        oscuridad.fill((0, 0, 0, 80))  # negro semitransparente
        self.imagen_hover.blit(oscuridad, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    def dibujar(self, screen):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):           # Detectar si el ratón está encima
            screen.blit(self.imagen_hover, self.rect.topleft)
        else:
            screen.blit(self.imagen_original, self.rect.topleft)

    def detectar_click(self, eventos):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            for event in eventos:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Codigo para ejecutar sonido
                    return True
        return False
