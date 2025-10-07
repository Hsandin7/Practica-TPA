import pygame

class Carta:
    PALOS = ["o", "c", "e", "b"]    # Oros(o), Copas(c), Espadas(e), Bastos(b)
    VALORES = list(range(1,13))

    def __init__(self, valor, palo):
        self._valor = valor
        self._palo = palo
        self.imagen_original = pygame.image.load(f"Graficos/cartas/{self.valor}{self.palo}.png")    # Imagen correspondiente cargada
        self.posicion = (0, 0)     # Pos de la imagen
        self.rect = self.imagen_original.get_rect(topleft=self.posicion)

        # Crea una versión oscurecida de la imagen, usando multiplicación RGBA
        self.imagen_hover = self.imagen_original.copy()
        oscuridad = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        oscuridad.fill((0, 0, 0, 80))  # negro semitransparente
        self.imagen_hover.blit(oscuridad, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    @property
    def valor(self):
        return self._valor

    @property
    def palo(self):
        return self._palo

    def asignar_posicion(self, posx, posy):     # Asigna la posición de la imagen
        self.posicion = (posx, posy)
        self.rect.topleft = self.posicion

    def dibujar(self, screen):                  # Función para mostrar la carta
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            screen.blit(self.imagen_original, self.posicion)
            screen.blit(self.imagen_hover, self.posicion)
        else:
            screen.blit(self.imagen_original, self.posicion)

    def detectar_click(self, eventos):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            for event in eventos:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Codigo para ejecutar sonido
                    return True
        return False
    
    def __str__(self):              # Cabia como se muestra la carta cuando se hace un print (Solo para debugging)
            return f"{self._valor}{self._palo}"
    

# # Testing
# sep = Carta(4, "o")
# print(sep)