from src._utilidades import reproducir_sonido
import pygame

class Boton:
    """Clase Boton: crea, asigna las posiciones del boton y detecta si estan conectados.
        
        Inicializa los atributos: 
        - x pone la posicion en x.
        - y pone la posicion en y.
        - imagen_original asigna la ruta de la imagen al boton.
        - _sonido_click le asigna un sonido al boton.
        - imagen_hover crea una version oscurecida de la imagen.
        
    """

    _cache_imagenes = {}
    _cache_hover = {}
    @classmethod
    def _get_cache_botones(cls, ruta_imagen, hover):
        cache = cls._cache_hover if hover else cls._cache_imagenes
        if ruta_imagen not in cache:
            imagen = pygame.image.load(ruta_imagen).convert_alpha()
            if hover:
                imagen_hover = imagen.copy()
                oscuridad = pygame.Surface(imagen.get_size(), pygame.SRCALPHA)
                oscuridad.fill((0, 0, 0, 80))  # negro semitransparente
                imagen_hover.blit(oscuridad, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                cache[ruta_imagen] = imagen_hover
            else:
                cache[ruta_imagen] = imagen
        return cache[ruta_imagen]

    def __init__(self, ruta_imagen, posx, posy, sonido = "Sonidos/sonido_boton.mp3"):
        self.x = posx
        self.y = posy
        self.imagen_original = self._get_cache_botones(ruta_imagen, False)      # Carga la imagen normal
        self.imagen_hover = self._get_cache_botones(ruta_imagen, True)          # Carga la imagen con el filtro hover
        self.rect = self.imagen_original.get_rect(topleft=(self.x,self.y))      # Crea el rect correspondiente
        self._sonido_click = sonido

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
