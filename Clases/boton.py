import pygame

class Boton:
    def __init__(self, ruta_imagen, posicion):
        # Carga la imagen base con transparencia
        self._imagen = pygame.image.load(ruta_imagen).convert_alpha()
        self.rect = self._imagen.get_rect(topleft=posicion)
        self.sonido_click = None

        # Guarda la imagen original
        self.imagen_original = self._imagen.copy()

        # Crea una versión oscurecida de la imagen, usando multiplicación RGBA
        self.imagen_hover = self.imagen_original.copy()
        oscuridad = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        oscuridad.fill((0, 0, 0, 80))  # negro semitransparente
        self.imagen_hover.blit(oscuridad, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    # --- PROPERTY ---
    @property
    def imagen(self):
        return self._imagen

    @imagen.setter
    def imagen(self, nueva_imagen):
        self._imagen = nueva_imagen

    # --- MÉTODOS ---
    def dibujar(self, pantalla):
        """Dibuja el botón, oscureciéndolo solo en las zonas visibles si el mouse está encima."""
        mouse_pos = pygame.mouse.get_pos()

        # Detectar si el ratón está encima
        if self.rect.collidepoint(mouse_pos):
            pantalla.blit(self.imagen_hover, self.rect.topleft)
        else:
            pantalla.blit(self.imagen_original, self.rect.topleft)

    def detectar_click(self, eventos):
        """Devuelve True si el botón fue clicado con el mouse."""
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            for event in eventos:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    return True
        return False
