import pygame


class Boton:
    """Clase Boton: Crea cada boton, carta y comodin del juego.

    Inicializa los atributos:
    - x pone la posicion en x.
    - y pone la posicion en y.
    - imagen_original asigna la ruta de la imagen al boton haciendo uso del cache.
    - imagen_hover crea una version oscurecida de la imagen haciendo uso del cache.
    - _sonido_click le asigna un sonido al boton.
    """

    _cache_imagenes = {}
    _cache_hover = {}
    _sonidos = {}

    @classmethod
    def _get_cache_botones(cls, ruta_imagen, hover):
        cache = cls._cache_hover if hover else cls._cache_imagenes
        if ruta_imagen not in cache:
            imagen = pygame.image.load(ruta_imagen).convert_alpha()
            if hover:
                imagen_hover = imagen.copy()
                oscuridad = pygame.Surface(imagen.get_size(), pygame.SRCALPHA)
                oscuridad.fill((0, 0, 0, 80))  # negro semitransparente
                imagen_hover.blit(
                    oscuridad, (0, 0), special_flags=pygame.BLEND_RGBA_MULT
                )
                cache[ruta_imagen] = imagen_hover
            else:
                cache[ruta_imagen] = imagen
        return cache[ruta_imagen]

    @classmethod
    def _get_cache_sonido(cls, ruta: str):
        if ruta not in cls._sonidos:
            cls._sonidos[ruta] = pygame.mixer.Sound(ruta)
        return cls._sonidos[ruta]

    def __init__(self, ruta_imagen, posx, posy, sonido="Sonidos/sonido_boton.mp3"):
        self.x = posx
        self.y = posy
        self.imagen_original = self._get_cache_botones(
            ruta_imagen, False
        )  # Carga la imagen normal
        self.imagen_hover = self._get_cache_botones(
            ruta_imagen, True
        )  # Carga la imagen con el filtro hover
        self.rect = self.imagen_original.get_rect(
            topleft=(self.x, self.y)
        )  # Crea el rect correspondiente
        self._sonido_click = sonido

    def asignar_posicion(self, posx, posy):  # Asigna la posicion de la imagen
        """Funcion asignar_posicion: Asigna la posicion posx y posy al boton."""
        self.x = posx
        self.y = posy
        self.rect.topleft = (self.x, self.y)

    def dibujar(self, screen):
        """Funcion dibujar: Muestra el boton y en caso de que el raton este
        encima, lo oscurece."""
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):  # Detectar si el raton esta encima
            screen.blit(self.imagen_original, (self.x, self.y))
            screen.blit(self.imagen_hover, (self.x, self.y))
        else:
            screen.blit(self.imagen_original, (self.x, self.y))

    def detectar_click(self, eventos):
        """Funcion detectar_click: Comprueba si el boton ha sido presionado para
        llevar a cabo la funcion correspondiente y reproduce el sonido."""
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            for event in eventos:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    sonido = self._get_cache_sonido(
                        self._sonido_click
                    )  # Reproducir sonido
                    sonido.play()
                    return True
        return False
