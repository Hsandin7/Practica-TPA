from src._utilidades import reproducir_sonido
import pygame

class Boton:
    """Clase Boton: crea, asigna las posiciones del boton y detecta si estan conectados.
        
        Inicializa los atributos: 
        - x pone la posicion en x
        - y pone la posicion en y
        - imagen_original asigna la ruta de la imagen al boton
        - _sonido_click le asigna un sonido al boton.
        - imagen_hover crea una version oscurecida de la imagen
        
    """
    def __init__(self, ruta_imagen, posx, posy, sonido = "Sonidos/sonido_boton.mp3"):
        self.x = posx
        self.y = posy
        self.imagen_original = pygame.image.load(ruta_imagen).convert_alpha()   # Carga la imagen
        self.rect = self.imagen_original.get_rect(topleft=(self.x,self.y))             # Crea el rect correspondiente
        self._sonido_click = sonido

        # Crea una version oscurecida de la imagen, usando multiplicacion RGBA
        self.imagen_hover = self.imagen_original.copy()
        oscuridad = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        oscuridad.fill((0, 0, 0, 80))  # negro semitransparente
        self.imagen_hover.blit(oscuridad, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    def asignar_posicion(self, posx, posy):     # Asigna la posicion de la imagen
        """Funcion asignar_posicion: pone la posicion x, y en el boton."""

        self.x = posx
        self.y = posy
        self.rect.topleft = (self.x,self.y)

    def dibujar(self, screen):
        """Funcion dibujar: muestra el boton y lo oscurece 
            en caso de que el raton este encima."""
        
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):           # Detectar si el raton esta encima
            screen.blit(self.imagen_original, (self.x, self.y))
            screen.blit(self.imagen_hover, (self.x, self.y))
        else:
            screen.blit(self.imagen_original, (self.x, self.y))

    def detectar_click(self, eventos):
        """Funcion detectar_click: comprueba si se ha dado click en el boton para 
            hacer la funcion correspondiente del boton."""
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            for event in eventos:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    reproducir_sonido(self._sonido_click)       # Reproducir sonido
                    return True
        return False
