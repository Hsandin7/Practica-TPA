import pygame

class Boton:
    def __init__(self, ruta_imagen, posicion, sonido = "Sonidos/Sonido_Boton.mp3"):
        self._posicion = posicion
        self.imagen_original = pygame.image.load(ruta_imagen).convert_alpha()   # Carga la imagen
        self.rect = self.imagen_original.get_rect(topleft=self._posicion)             # Crea el rect correspondiente
        self._sonido_click = pygame.mixer.Sound(sonido)

        # Crea una versión oscurecida de la imagen, usando multiplicación RGBA
        self.imagen_hover = self.imagen_original.copy()
        oscuridad = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        oscuridad.fill((0, 0, 0, 80))  # negro semitransparente
        self.imagen_hover.blit(oscuridad, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    def asignar_posicion(self, posx, posy):     # Asigna la posición de la imagen
        self._posicion = (posx, posy)
        self.rect.topleft = self._posicion

    def dibujar(self, screen):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):           # Detectar si el ratón está encima
            screen.blit(self.imagen_original, self._posicion)
            screen.blit(self.imagen_hover, self._posicion)
        else:
            screen.blit(self.imagen_original, self._posicion)

    def detectar_click(self, eventos):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            for event in eventos:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self._sonido_click.play()   # Reproducir sonido
                    return True
        return False
